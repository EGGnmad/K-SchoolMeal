import asyncio
from typing import Optional

from KSchoolMeal.getSchoolCode import school_code
from KSchoolMeal.getSchoolMeal import school_meal



class sync:
    @staticmethod
    def school_meal(region_code:str, school_code:str, date:str):
        return asyncio.run(school_meal(region_code, school_code, date))

    @staticmethod
    def school_code(school_name: str, region:Optional[str]=None):
        return asyncio.run(school_code(school_name, region))