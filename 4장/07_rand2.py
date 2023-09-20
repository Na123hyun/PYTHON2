'''
2023-09-20
김나현
선택문 if ~ else
    random을 이용한 가위바위보 게임

    random함수로 생성된 정수를 가지고 게임을 진행한다.
    0 => 가위
    1 => 바위
    2 => 보

    두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행한다.
'''

import random #random 함수 가져오기(포함시키기)

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("player1의 이름을 적으십시오. : ")
player2 = input("player2의 이름을 적으십시오. : ")

#range : 반복 -> 범위 -> for문
num1 = random.randrange(3) #player1의 랜덤 수
num2 = random.randrange(3) #player2의 랜덤 수

#player1의 가위 바위 보 출력
print(player1, ":", end='')
if num1 == 0 :
    print("가위")
if num1 == 1 :
    print("바위")
if num1 == 2 : 
    print("보")

#player2의 가위 바위 보 출력
print(player2, ":", end='')
if num2 == 0 :
    print("가위")
elif num2 == 1 :
    print("바위")
else : 
    print("보")

#승자를 판단하여 출력
if (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1) :
    print(f"{player1}님 승리")
elif num1 == num2 :
    print("무승부입니다.")
else:
    print(f"{player2}님 승리")