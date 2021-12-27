import asyncio

import KSchoolMeal

#async
async def main():
    school_data = await KSchoolMeal.school_code( input('학교: ') )

    meal_data = await KSchoolMeal.school_meal(school_data.region_code, school_data.school_code, input('시간입력(yyyyMM): '))
    print(meal_data[0])

if __name__ == '__main__':
    asyncio.run(main())

#sync
school_data = KSchoolMeal.sync.school_code( input('학교: ') )

meal_data = KSchoolMeal.sync.school_meal(school_data.region_code, school_data.school_code, input('시간입력(yyyyMM): '))

print(meal_data)