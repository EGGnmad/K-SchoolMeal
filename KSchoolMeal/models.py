from typing import Optional

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

def region_code(office_name:str):
    try:
        return region_codes[office_name]
    except KeyError:
        return None

from dataclasses import dataclass

@dataclass
class SchoolMealInfo:
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



@dataclass
class SchoolInfo:
    region_code : str                       #시도교육청코드
    region_office_name : str                #시도교육청명
    school_code : str                       #표준학교코드
    school_name : str                       #학교명
    school_level: str                       #학교종류명
    location_name : str                     #소재지명
    foundation_type : str                   #설립명(ex: 사립, 공립)
    address : str                           #도로명주소
    tel: str                                #전화번호
    homepage: str                           #홈페이지주소
    coeducation: str                        #남녀공학구분명
    school_type : str                       #고등학교구분명
    school_anniversary : str                #개교기념일

    def __init__(self, data):
        self.region_code = data['ATPT_OFCDC_SC_CODE']
        self.region_office_name = data['ATPT_OFCDC_SC_NM']
        self.school_code = data['SD_SCHUL_CODE']
        self.school_name = data['SCHUL_NM']
        self.school_level = data['SCHUL_KND_SC_NM']
        self.location_name = data['LCTN_SC_NM']
        self.foundation_type = data['FOND_SC_NM']
        self.address = data['ORG_RDNMA']
        self.tel = data['ORG_TELNO']
        self.homepage = data['HMPG_ADRES']
        self.coeducation = data['COEDU_SC_NM']
        self.school_type = data['HS_SC_NM']
        self.school_anniversary = data['FOAS_MEMRD']
