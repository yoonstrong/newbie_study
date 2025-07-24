# 3-a
def my_multi(number_1, number_2):
    return number_1 * number_2
result_1 = my_multi(2, 3)
print(result_1)
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    if number <= 0:
        return True
    else:
        return False

result_2 = is_negative(3)
print(result_2)        
        
# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(default = '기본 값'):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)

# 3-b
pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title=None):
    global pro_num
    pro_num += 1
    data = {}
    data = {'과목' : subject, '일차' : day, '제목' : title, '문제 번호' : pro_num}
    return data

result_1 = create_data('python', 3)
result_2 = create_data('web', 1, 'web 연습하기')
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)

# 3-c
def recur_example(number):
    '''
        함수(2) 실행
            number에 2 할당
            if 2 == 1 조건문 만족하지 않음
            else문 2 + 함수(2-1) 
                결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

                함수(2-1) 실행
                    number에 1 할당
                    if 1 == 1 조건문 만족하므로 1 반환
            
            else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
            2 + 1 반환
        결과 : 3  
    '''
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if  exponent == 0:
        return 1
    else:
        return base * power(base, exponent -1)
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6

# 3-1
number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


increase_user()
print("현재 가입 된 유저 수:", number_of_people)

# 3-2
number_of_people = 0

print("현재 가입 된 유저 수:", number_of_people)

def create_user(name, age, address):
    user_info ={}
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f"{name}님 환영합니다!")
    return user_info

result_1 = create_user('홍길동', 30, '서울')

print(result_1)

def increase_user():
    global number_of_people
    number_of_people += 1

increase_user()
print("현재 가입 된 유저 수:", number_of_people)

# 3-3


number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book

result_1 = decrease_book(3)
print("남은 책의 수 :", result_1)


def rental_book(name, number):
    decrease_book(3)
    print(f"{name}님이 {number}권의 책을 대여하였습니다.")


rental_book('홍길동', 3)

# 3-4
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    user_info ={}
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f"{name}님 환영합니다!")
    return user_info
    
users = list(map(create_user, name, age, address))
print(users)

# create_user는 괄호 없이 넣었기 때문에 "함수 자체"를 map()에게 전달
# map()이 알아서 name[0], age[0], address[0] 식으로 하나씩 꺼내서 create_user()에 넣음

# 3-5
# 기본 데이터
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 실습 4: 사용자 생성 함수
def create_user(name, age, address):
    user_info = {}
    user_info = {'name': name, 'age': age, 'address': address}
    print(f"{name}님 환영합니다!")
    return user_info

# many_user 변수에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트 할당
many_user = list(map(create_user, name, age, address))

# 실습 3: 책 재고 관리
number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book
'''
map과 lambda를 사용해 새로운 딕셔너리 생성 (name과 age만 포함)
map(lambda user: {'name': user['name'], 'age': user['age']}, many_user)는
many_user의 각 딕셔너리에 대해 lambda 함수를 적용
각 딕셔너리에서 name과 age 키의 값만 추출해서 새로운 딕셔너리 생성
'''
info = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))

# 수정된 rental_book 함수 (info 인자 하나만 받음)
def rental_book(info):
    # 나이를 10으로 나눈 몫을 대여할 책의 수로 사용
    rental_count = info['age'] // 10
    
    # decrease_book 함수 호출
    remain_books = decrease_book(rental_count)
    
    print(f"남은 책의 수 : {remain_books}")
    print(f"{info['name']}님이 {rental_count}권의 책을 대여하였습니다.")


# map 함수를 사용해 rental_book 함수에 각각 전달하여 호출
list(map(rental_book, info))