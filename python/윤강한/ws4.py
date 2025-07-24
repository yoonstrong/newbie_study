# 4-a

# from conf import settings
# from utils import create_url

# NAME = 'develper'
# MAIN_URL = 'http://127.0.0.1:8000'


# def create_url(name, main_url, page_num=1):
#     new_url = f'{main_url}/{name}?page={page_num}'
#     return new_url
# result = create_url(NAME, MAIN_URL)

# print(result)

# 4-b

# food_list = [
#     {
#         '종류': '한식',
#         '이름': '잡채'
#     },
#     {
#         '종류': '채소',
#         '이름': '토마토'
#     },
#     {
#         '종류': '중식',
#         '이름': '자장면'
#     },
# ]

# # 아래에 코드를 작성하시오.



# food_list[1]['종류'] = '과일'
# food_list[2]['이름'] = '자장면엔 고춧가루지'

# for food in food_list:
#     print(f"{food['이름']} 은/는 {food['종류']} (이)다.") # dicct 키 접근시 [] 사용

# print(food_list)


# i = 0
# while i < len(food_list):
#     food = food_list[i]
#     print(f"{food['이름']} 은/는 {food['종류']} (이)다.")
#     i += 1

# print(food_list)

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

# matrix_len = len(matrix)
# matrix_len = 0
# for i in matrix:
    
#     matrix_len += 1
# print(matrix_len)


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

