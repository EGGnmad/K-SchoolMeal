import asyncio

import KSchoolMeal

async def main():
    print(await KSchoolMeal.school_code('분당중학교'))

if __name__ == '__main__':
    asyncio.run(main())