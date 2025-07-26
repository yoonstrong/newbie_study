# 4-a

from conf import settings
from utils import create_url

NAME = 'develper'
MAIN_URL = 'http://127.0.0.1:8000'

def create_url(name, main_url, page_num=1):
    new_url = f'{main_url}/{name}?page={page_num}'
    return new_url
result = create_url(NAME, MAIN_URL)

print(result)

# 4-b

food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

food_list[1]['종류'] = '과일'
food_list[2]['이름'] = '자장면엔 고춧가루지'

for food in food_list:
    print(f"{food['이름']} 은/는 {food['종류']} (이)다.") # dicct 키 접근시 [] 사용

print(food_list)


i = 0
while i < len(food_list):
    food = food_list[i]
    print(f"{food['이름']} 은/는 {food['종류']} (이)다.")
    i += 1

print(food_list)

# 4-c

matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 2차원 리스트 : 리스트 안에 또 다른 리스트들이 들어 있는 구조

matrix_len = len(matrix)
matrix_len = 0
for i in matrix:
    
    matrix_len += 1
print(matrix_len)


for number in matrix:
    if len(number) <= 4:
        print(f"{number} 리스트는 {len(number)}만큼의 요소를 가지고 있습니다.")


#  2차원 리스트 : 리스트 안에 또 다른 리스트들이 들어 있는 구조
#  첫 번째 for문은 바깥 리스트를 순회하면서 각 행의 인덱스애 접근
# | x 값 | matrix\[x]                |
# | --- | ------------------------- |
# | 0   | \['0, 1', '0, 2', '0, 3'] |
# | 1   | \['1, 0', '1, 1', ...]    |
# | ... | ...                       |

# 두 번째 for문은 각 행에 대해 열을 순회
# | x | matrix\[x]                | y의 범위 (`len(matrix[x])`) |
# | - | ------------------------- | ------------------------ |
# | 0 | \['0, 1', '0, 2', '0, 3'] | 0 \~ 2                   |
# | 1 | \['1, 0', ..., '1, 3']    | 0 \~ 3                   |
# | 2 | \['2, 0', ..., '2, 4']    | 0 \~ 4                   |

for x in range(len(matrix)):      # range(0,6)
    for y in range(len(matrix[x])): # 각 리스트의 range
        print(f"matrix의 {x}, {y} 번째 요소의 값은 {matrix[x][y]} 입니다.")
        
# 4-1
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data)
# 변환 데이터의 타입
print(type(parsed_data))

# 특정 데이터 출력
print(parsed_data['username'])
print(parsed_data['company']['name'])
print(parsed_data['name'])

# 4-2 
import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    API_URL = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(API_URL)
    parsed_data = response.json()
    name = parsed_data['name']
    dummy_data.append(name)
    
print(dummy_data)

# 4-3
import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    if lat < 80 and lng > -80:
            user_info = {'company' : company, 'lat' : lat, 'lng' : lng, 'name' : name}
            dummy_data.append(user_info)
print(dummy_data)

# 4-4
import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 사용자 더미 데이터 수집
dummy_data = []

for i in range(1, 11):
    API_URL = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']
    name = parsed_data['name']
    user_info = {'company': company, 'name': name}
    dummy_data.append(user_info)

# 블랙리스트 여부 확인 함수
def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

# 사용자 등록 함수
def create_user(user_list):
    censored_user_list = {}

    for user in user_list:
        company = user['company']
        name = user['name']

        if censorship(company, name):
            if company not in censored_user_list:
                censored_user_list[company] = []       # 회사 키가 없으면 추가
            censored_user_list[company].append(name)   # 회사명에 해당하는 리스트에 그 사람 이름 추가

    return censored_user_list

# 사용자 등록 결과 출력
result = create_user(dummy_data)
print(result)

# 4-5
def is_validation(user):
    errors = []

    # a) 회사 블랙리스트 먼저
    if user['company'] in black_list:
        return 'blocked'

    # b) 혈액형
    if user['blood_group'] not in blood_types:
        errors.append('blood_group')

    # c) 메일
    if '@' not in user['mail']:
        errors.append('mail')

    # d) 이름 길이
    if not (2 <= len(user['name']) <= 30):
        errors.append('name')

    # e) 웹사이트 개수
    if len(user['website']) < 1:
        errors.append('website')

    # f) 오류가 있으면 (False, [필드명]) 반환
    if errors:
        return (False, errors)

    # g) 모두 통과했으면 True 반환
    return True

def create_user(users):
    # 1) 최종에 담을 유저 리스트와 잘못된 유저 수 세는 변수
    clean_users = []
    bad_user_count = 0

    # 2) users 리스트의 각 user(딕셔너리)를 하나씩 살펴봅니다
    for user in users:
        result = is_validation(user)  # 검사 함수 실행

        # 3) 회사가 블랙리스트면 result == 'blocked'
        if result == 'blocked':
            bad_user_count += 1
            # 이 유저는 목록에 추가하지 않고 다음으로 넘어갑니다
            continue

        # 4) 검사 결과가 True면(문제 없으면)
        if result is True:
            clean_users.append(user)
        else:
            # 5) 검사 결과가 (False, [필드목록])이면
            bad_user_count += 1
            error_fields = result[1]  # 잘못된 필드 이름들이 들어있는 리스트

            # 6) 원본 user에서 값을 하나씩 꺼내 새 딕셔너리에 담음
            fixed_user = {}
            # 수정할 키 목록을 미리 작성해 두면 이해하기 더 쉽습니다
            for key in ['blood_group', 'company', 'mail', 'name', 'website']:
                # 잘못된 필드면 None, 아니면 원래 값을 복사
                if key in error_fields:
                    fixed_user[key] = None
                else:
                    fixed_user[key] = user[key]

            clean_users.append(fixed_user)

    # 7) 결과 출력
    print(f"잘못된 데이터로 구성된 유저의 수는 {bad_user_count} 입니다.")
    for u in clean_users:
        print(u)
    print("이하 결과 생략...")

create_user(user_data)

# 과제 1
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '난중일기'
    '백호집',
    '홍길동전',
    '만복자서포기',
]

for book in rental_list:           # for else 구문은 반복문이 break로 중단되지 않고 정상 완료됐을 때만 else 블록 실행
    if book not in list_of_book:   # 모든 도서가 대여 가능할 때는 break로 중단되지 않기 때문에 else문 실행
        
        print(f"{book} 은/는 보유하고 있지 않습니다.")
        break
else:
    print("모든 도서가 대여 가능한 상태입니다.")

# 과제 2
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',

]

missing_book = [book for book in rental_list if book not in list_of_book] # list comprehension을 사용 

if missing_book:    # 리스트가 비어있다고 해서 객체가 False인 것은 아니므로 is False를 사용하지 않는것을 권장
    for book in missing_book:
        print(f"{book} 을/를 보충하여야 합니다.")
else:
    print("모든 도서가 대여 가능한 상태입니다.")
    
