#test1
import asyncio

import KSchoolMeal

async def main():
    print( await KSchoolMeal.school_code('한국애니메이션고등학교') )

if __name__ == '__main__':
    asyncio.run(main())

#test2
print(KSchoolMeal.sync.school_code('분당중학교'))