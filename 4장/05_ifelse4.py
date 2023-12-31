'''
2023-09-20
김나현
선택문 if ~ else
    연도를 입력 받아 윤년인지 아닌지 판단하는 프로그램

    윤년?
    윤년은 4년마다 돌아오므로 12년마다 돌아오는 해이다.
    연도가 4로 나누어 0이면 윤년이고, 400으로 나누어 0이면 윤년이다.
    연도를 4로 나누어 떨어지면 윤년이다.
    연도를 4로 나누어 떨어져도, 100으로는 나누어 떨어지지 않아야 한다.
        -> (모두 만족 : and연산자, C언어는 &&)
    연도를 400으로 나누어 떨어지는 해는 무조건 윤년이다.
        -> (or연산자, C언어는 ||)
'''

#1. 연도르 입력 받는다.
year = int(input("연도를 입력하시오. : "))

#2. 판단한다.
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
    print(f"{year}년은 윤년입니다.") #포맷형식
else :
    print(f"{year}년은 윤년이 아닙니다.") #포맷형식