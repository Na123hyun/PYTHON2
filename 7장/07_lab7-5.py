'''
2023-11-01
컴퓨터공학부 202395004 김나현
LAB 7-5 함수는 튜플을 돌려줄 수 있다.
    반지름을 입력 받아 원의 넓이와 둘레를 계산하시오.
    넓이와 둘레를 계산하는 함수를 작성하시오.
    함수는 넓이와 둘레를 함께 돌려줍니다. (return)

    [함수]
        3. 반지름을 받아서 매개변수에 저장한다.
        4. 넓이와 둘레를 계산한다.
        5. 넓이와 둘레를 돌려준다. (함수를 호출한 곳으로)
            return 넓이, 둘레

    [메인]
        1. 반지름을 입력 받는다.
        2. 함수 호출 -> 반지름을 가지고 호출한다.
        6. 돌려받은 넓이와 둘레를 튜플로 저장한다.
            (넓이, 둘레)
        7. 출력한다.

        area = 넓이 circum = 둘레
'''
#반지름이 r인 원이 넓이와 두레를 동시에 반환하는 함수 (area, circum)
def calCircle(r) :
    #넓이 계산
    area = 3.14 * r * r
    #둘레 계산
    circum = 2 * 3.14 * r
    return (area, circum)

#반지름을 입력 받는다.
radius = float(input("반지름을 입력하시오. : "))
(area, circum) = calCircle(radius)

#.2f는 소수점 2자리 출력
print(f"반지름이 {radius}인 원의 넓이는 {area:.2f}이고, 원의 둘레는 {circum:.2f}입니다.")

circle = calCircle(radius)
print(f"반지름이 {radius}인 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f}입니다.")

#줄바꿈
print()

#파이값 가져오기
import math
#반지름이 r인 원이 넓이와 두레를 동시에 반환하는 함수 (area, circum)
def calCircle(r) :
    #넓이 계산
    area = math.pi * r * r
    #둘레 계산
    circum = 2 * math * r
    return (area, circum)

#반지름을 입력 받는다.
radius = float(input("반지름을 입력하시오. : "))
(area, circum) = calCircle(radius)

#.2f는 소수점 2자리 출력
print(f"반지름이 {radius}인 원의 넓이는 {area:.2f}이고, 원의 둘레는 {circum:.2f}입니다.")

circle = calCircle(radius)
print(f"반지름이 {radius}인 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f}입니다.")