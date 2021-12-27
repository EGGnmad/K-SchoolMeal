office_codes = \
    {
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

def office_code(office_name:str):
    try:
        return office_codes[office_name]
    except KeyError:
        return None

from dataclasses import dataclass

@dataclass
class SchoolMealInfo:
    office_code : str #office of education code
    office_name : str #office of education name
    school_code : str
    school_name : str
    meal_code : str
    meal_name : str
    day : str
    person_number: int
    dish_name : str
    origin_info : str
    calorie_info : str
    nutrient_info : str

