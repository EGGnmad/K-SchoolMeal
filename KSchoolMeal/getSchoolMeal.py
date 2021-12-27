import aiohttp
import asyncio
import config

from KSchoolMeal import models, exceptions
from KSchoolMeal.models import SchoolMealInfo


async def school_meal(region_code: str, school_code:str, date: str) -> list[SchoolMealInfo]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.get(config.base_url, params={'KEY':config.app_key, 'Type': 'json', 'ATPT_OFCDC_SC_CODE': region_code, 'SD_SCHUL_CODE': school_code, 'MLSV_YMD': date}) as response:
            result =  await response.json(content_type='text/html')
            try:
                status = result['mealServiceDietInfo'][0]['head'][1]['RESULT']['CODE'] #check response RESULT CODE

                result = result['mealServiceDietInfo'][1]['row']

                meal_datas = []

                for data in result:
                    meal_datas.append(await school_meal_info(data))

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

    nutrients['탄수화물(g)'] = float(str(nutrients_list[0]).replace('탄수화물(g) : ', ''))
    nutrients['단백질(g)'] = float(str(nutrients_list[1]).replace('단백질(g) : ', ''))
    nutrients['지방(g)'] = float(str(nutrients_list[2]).replace('지방(g) : ', ''))
    nutrients['비타민A(R.E)'] = float(str(nutrients_list[3]).replace('비타민A(R.E) : ', ''))
    nutrients['티아민(mg)'] = float(str(nutrients_list[4]).replace('티아민(mg) : ', ''))
    nutrients['리보플라빈(mg)'] = float(str(nutrients_list[5]).replace('리보플라빈(mg) : ', ''))
    nutrients['비타민C(mg)'] = float(str(nutrients_list[6]).replace('비타민C(mg) : ', ''))
    nutrients['칼슘(mg)'] = float(str(nutrients_list[7]).replace('칼슘(mg) : ', ''))
    nutrients['철분(mg)'] = float(str(nutrients_list[8]).replace('철분(mg) : ', ''))


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