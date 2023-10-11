'''
2023-10-11
컴퓨터공학부 202395004 김나현
LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수

    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력받아 최대값, 최소값을 찾아 돌려주는 함수

    (함수)
            5) 두 값을 전달받아 매개 변수에 저장한다.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.

    (메인)
        1. 무한 반복
            1) 랜덤으로 10 ~ 99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은 지 최소값을 알고 싶은 지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수를 호출한다.
            8) 돌려받은 최대값 또는 최소값을 출력한다.
'''
#random 랜덤 모듈 선언
import random

#두 값을 전달받아 매개 변수에 저장한다.
def getMinMax(my_list, method='max'):

    #최대값을 찾는다.
    if method == 'max' :
        maxValue = max(my_list)
        return '최대값 : ' , maxValue
    
    #최소값을 찾는다.
    elif method == 'min' :
        minValue = min(my_list)
        return '최소값 : ' , minValue
    else :
       #값을 돌려준다.
       print('illegal method')

#무한 반복
while True :

    #"_" 변수의 이름을 특별히 지정하지 않고, 단순히 반복 횟수를 나타내는 용도로 사용
    #랜덤으로 10 ~ 99까지 10개의 수를 리스트로 생성
    list_data = [random.randint(10, 99) for _ in range(10)]

    #생성된 리스트를 출력
    print('생성된 리스트 : ', list_data)
    
    #사용자로부터 최대값을 알고 싶은 지 최소값을 알고 싶은 지 묻는다.
    input_result = input('최대값을 원하면 max, 최소값을 원하면 min을 입력하시오 : ')

    #입력받은 max 또는 min과 생성된 리스트를 가지고 함수를 호출한다.
    #돌려받은 최대값 또는 최소값을 출력한다.
    print(getMinMax(list_data, input_result))