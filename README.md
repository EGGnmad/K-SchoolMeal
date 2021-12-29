<h3> 🍞 K-School Meal </h3>

<h4>k-급식</h4> 

---
[![](https://img.shields.io/badge/Python-3.7|3.8|3.9|3.10-blue?style=flat-square&logo=python)](https://www.python.org/)
[![](https://img.shields.io/badge/KSchoolMeal-1.0.0Alpha-blue?style=flat-square)](https://pypi.org/project/k-SchoolMeal/)


<h3>다운</h3>

```
python3 -m pip install k-SchoolMeal
```

<br>

<h3>예시</h3>

---

```py
#분당중학교

#async
async def main():
    school_info = await KSchoolMeal.school_code('분당중학교')
    meal = await KSchoolMeal.school_meal(school_info.region_code, school_info.school_code, '2021.11.01') #-> List[SchoolMealInfo] 

#sync
def main():
    school_info = KSchoolMeal.sync.school_code('분당중학교')
    
    meal = KSchoolMeal.sync.school_meal(school_info.region_code, school_info.school_code, '2021.11.01') #-> List[SchoolMealInfo]

```

<br>

<h3>정보</h3>

---

<h4>교육청 코드</h4>

```py
region_codes = {
        '서울특별시': 'B10',
        '부산광역시': 'C10',
        '대구광역시': 'D10',
        '인천광역시': 'E10',
        '광주광역시': 'F10',
        '대전광역시': 'G10',
        '울산광역시': 'H10',
        '세종특별자치시': 'I10',
        '경기도': 'J10',
        '강원도': 'K10',
        '충청북도': 'M10',
        '충청남도': 'N10',
        '전라북도': 'P10',
        '전라남도': 'Q10',
        '경상북도': 'R10',
        '경상남도': 'S10',
        '제주특별자치도': 'T10'
    }
```

<h4> 응답 정보 </h4>

```py
class SchoolMealInfo:               # 급식 정보
    region_code : str               #시도교육청코드
    region_office_name : str        #시도교육청명
    school_code : str               #표준학교코드
    school_name : str               #학교명
    meal_code : str                 #식사코드
    meal_type : str                 #식사명
    date : str                      #급식일자
    person_number: int              #급식인원수
    dish : list[str]                #요리명
    origin_info : list[str]         #원산지정보
    calorie : str                   #칼로리정보
    nutrients : dict[str, float]    #영양정보
```

```py
#예시
nutrients = {
        '탄수화물(g)': 104.3,
        '단백질(g)': 35.8,
        '지방(g)': 18.7,
        '비타민A(R.E)': 285.8,
        '티아민(mg)': 0.4,
        '리보플라빈(mg)': 0.6,
        '비타민C(mg)': 22.5,
        '칼슘(mg)': 220.0,
        '철분(mg)': 3.9
    }
```

```py
class SchoolInfo:                   # 학교 정보
    region_code : str               #시도교육청코드
    region_office_name : str        #시도교육청명
    school_code : str               #표준학교코드
    school_name : str               #학교명
    school_level: str               #학교종류명
    location_name : str             #소재지명
    foundation_type : str           #설립명(ex: 사립, 공립)
    address : str                   #도로명주소
    tel: str                        #전화번호
    homepage: str                   #홈페이지주소
    coeducation: str                #남녀공학구분명
    school_type : str               #고등학교구분명
    school_anniversary : str        #개교기념일
```