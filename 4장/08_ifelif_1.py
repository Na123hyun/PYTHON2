'''
2023-09-27
컴퓨터공학부 202395004 김나현
#설명
점수를 입력받아 학점을 출력하시오.
    90 ~ 100 : A학점
    80 ~ 89 : B학점
    70 ~ 79 : C학점
    60 ~ 69 : D학점
    0 ~ 59 : F학점
#알고리즘
    1. 점수를 입력 받는다.
    2. 판단하여 출력한다.
'''

# 점수를 입력 받는다.
score = int(input("점수를 입력하시오. : "))

# 판단
# 이 코드는 논리 오류가 발생한다. - 300점 입력하면 A학점으로 나온다.
print("::: 첫 번째 성적처리 :::")

if score >= 90 :
    print("A학점")

elif score >= 80 :
    print("B학점")

elif score >= 70 :
    print("C학점")

elif score >= 60 :
    print("D학점")
#남아있는 것들 나머지 처리

else :
    print("F학점")

print() #줄 바꿈

#정확한 범위를 지정하자. - 성적의 범위를 벗어나면 "잘못된 점수"입력한다.
print("::: 두 번째 성적처리 :::")

#이상, 이하
if (90 <= score <= 100) :
    print("A학점")

#프로그래밍의 효율을 위해 elif를 쓰는게 좋다.
# score >= 80 && score <= 89 ~ C언어
elif (score >= 80 and score < 89) :
    print("B학점")

elif (70 <= score <= 79) :
    print("C학점")

elif (60 <= score <= 69) :
    print("D학점")

elif (0 <= score <= 59) :
    print("F학점")

else :
    print("점수를 잘못 입력하셨습니다.")

print() #줄 바꿈

#점수는 무조건 0 ~ 100점 사이입니다. - 아니면 잘못된 입력입니다.
#내포된 if, 범위 지정 if
print("::: 세 번째 성적처리 :::")

if 0 <= score <= 100 :

    if score >= 90 :
        print("A학점")

    elif score >= 80 :
        print("B학점")

    elif score >= 70 :
        print("C학점")

    elif score >= 60 :
        print("D학점")

    #A,B,C,D학점이 아니면
    else :
        print("F학점")

#0 ~ 100점 사이의 점수가 아니면
else :
    print("점수를 잘못 입력하셨습니다.")

