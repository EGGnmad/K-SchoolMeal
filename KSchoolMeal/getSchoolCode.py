from typing import Optional

import aiohttp
from KSchoolMeal import exceptions, models
from KSchoolMeal.models import SchoolInfo
import os


async def school_code(school_name: str, region:Optional[str]=None) -> SchoolInfo:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.get('https://open.neis.go.kr/hub/schoolInfo', params=
            {'Type': 'json', 'ATPT_OFCDC_SC_CODE': models.region_code(region), 'SCHUL_NM': school_name} if models.region_code(region) != None else {'Type': 'json', 'SCHUL_NM': school_name}
                               ) as response:
            result = await response.json(content_type='text/html')
            try:
                status = result['schoolInfo'][0]['head'][1]['RESULT']['CODE'] #check response RESULT CODE

                if result['schoolInfo'][0]['head'][0]['list_total_count'] > 1: #check result size is smaller than 1
                    raise exceptions.TooManyResultException(result['schoolInfo'][0]['head'][0]['list_total_count'])

                result = SchoolInfo(result['schoolInfo'][1]['row'][0])
                return result

            except KeyError as e:
                raise exceptions.RequestsException(str(result['RESULT']['CODE']) + ': ' + str(result['RESULT']['MESSAGE']))
