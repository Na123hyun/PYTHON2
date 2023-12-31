'''
2023-09-20
김나현
선택문 if ~ else
    교통카드의 종류로 '청소년', '성인'카드가 있다고 한다.
    사용자에게 카드의 종류를 입력 받아 청소년이면 "청소년입니다."를
    성인이면 "성인입니다."를 출력하자

    청소년 카드로 조건을 할 것인지 성인 카드로 할 것 인지 정하여라

    문자 - a, b, c
    문자열 - 이름

    정수 ~ 변환해야 하는 것은 int를 쓴다.
'''

#1. 문자로 입력 받는다. -> input만 사용해도 된다. -> 카드의 종류를 입력 받는다.
card = input("카드의 종류를 입력(청소년, 성인 중 하나)하시오. : ")

#2. 입력 받은 카드 종류가 청소년인지 성인인지 판단한다.
if card == '청소년' :   #if(card == '성인') -> C언어에서 사용
    print("청소년입니다.")
elif card == '성인' : #그렇지 않고 만약에 elif / else if
    print("성인입니다.")
else :
    print("다시 입력해주십시오.")

'''
#판단 1.
if card == '성인' :
    print("성인입니다.")
else :
    print("청소년입니다.")

#판단 2.
if card == '청소년' :
    print("청소년입니다.")
if card == '성인' :
    print("성인입니다.")
'''