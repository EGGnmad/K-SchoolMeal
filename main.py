import asyncio
import os
import KSchoolMeal


#async
async def main():
    school_data = await KSchoolMeal.school_code('한국애니메이션')

    meal_data = await KSchoolMeal.school_meal(school_data.region_code, school_data.school_code, '2021.12.13')
    print(meal_data)

if __name__ == '__main__':
    asyncio.run(main())
