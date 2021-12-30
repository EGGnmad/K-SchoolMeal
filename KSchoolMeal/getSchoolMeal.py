from typing import Optional

import aiohttp
from KSchoolMeal import exceptions
from KSchoolMeal.models import SchoolMealInfo
import os



async def school_meal(region_code: str, school_code:str, date: str) -> list[SchoolMealInfo]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        date = date.replace('.', '')
        async with session.get('https://open.neis.go.kr/hub/mealServiceDietInfo', params={'Type': 'json', 'ATPT_OFCDC_SC_CODE': region_code, 'SD_SCHUL_CODE': school_code, 'MLSV_YMD': date}) as response:
            result =  await response.json(content_type='text/html')
            try:
                status = result['mealServiceDietInfo'][0]['head'][1]['RESULT']['CODE'] #check response RESULT CODE

                result = result['mealServiceDietInfo'][1]['row']

                meal_datas = [await school_meal_info(data) for data in result]

                return meal_datas


            except KeyError:
                raise exceptions.RequestsException(str(result['RESULT']['CODE']) + ': ' + str(result['RESULT']['MESSAGE']))


async def school_meal_info(data) -> SchoolMealInfo:
    region_code = data['ATPT_OFCDC_SC_CODE']
    region_office_name = data['ATPT_OFCDC_SC_NM']
    school_code = data['SD_SCHUL_CODE']
    school_name = data['SCHUL_NM']
    meal_code = data['MMEAL_SC_CODE']
    meal_type = data['MMEAL_SC_NM']
    date = data['MLSV_YMD']
    person_number = data['MLSV_FGR']

    dish = data['DDISH_NM'].split('<br/>')
    origin_info = data['ORPLC_INFO'].split('<br/>')
    calorie = data['CAL_INFO']

    #nutrients
    nutrients_list = data['NTR_INFO'].split('<br/>')
    nutrients = {}

    for nutrient in nutrients_list:
        key, value =  str(nutrient).split(':')
        nutrients[key.replace(' ', '')] = float(value.replace(' ', ''))


    result = SchoolMealInfo(
        region_code=region_code,
        region_office_name=region_office_name,
        school_code=school_code,
        school_name=school_name,
        meal_code=meal_code,
        meal_type=meal_type,
        date=date,
        person_number=person_number,
        dish=dish,
        origin_info=origin_info,
        calorie=calorie,
        nutrients=nutrients
    )
    return result