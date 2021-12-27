'''
 [asyncio] python 3.7 >=
'''
import json
from typing import Optional

import aiohttp
import asyncio
import config
from KSchoolMeal import exceptions, models
from KSchoolMeal.models import SchoolInfo

async def school_code(school_name: str, region:Optional[str]=None) -> SchoolInfo:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.get(config.school_info_base_url, params= await check_region(region, school_name) ) as response:
            result = await response.json(content_type='text/html')
            try:
                status = result['schoolInfo'][0]['head'][1]['RESULT']['CODE'] #check response RESULT CODE

                if result['schoolInfo'][0]['head'][0]['list_total_count'] > 1: #check result size is smaller than 1
                    raise exceptions.TooManyResultException(result['schoolInfo'][0]['head'][0]['list_total_count'])

                result = SchoolInfo(result['schoolInfo'][1]['row'][0])
                return result

            except KeyError as e:
                raise exceptions.RequestsException(result['RESULT']['CODE'])


async def check_region(region, school_name:str) -> dict:
    if models.region_code(region) != None:
        return {'KEY':config.app_key, 'Type':'json', 'ATPT_OFCDC_SC_CODE': models.region_code(region), 'SCHUL_NM': school_name}
    else:
        return {'KEY':config.app_key, 'Type':'json', 'SCHUL_NM': school_name}


class sync:
    @staticmethod
    def school_code(school_name: str, region:Optional[str]=None):
        return asyncio.run(school_code(school_name, region))
