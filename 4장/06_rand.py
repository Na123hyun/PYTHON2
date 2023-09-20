'''
2023-09-20
김나현
선택문 if ~ else
    random을 이용한 가위바위보 게임

    random함수로 생성된 정수를 가지고 게임을 진행한다.
    0 => 가위
    1 => 바위
    2 => 보
'''

import random #random 함수 가져오기(포함시키기)

print(":: 가위 바위 보 게임 시작 ::")

#range : 반복 -> 범위 -> for문
num = random.randrange(3) #random으로 0, 1, 2를 생성하여 변수에 저장

#가위 바이 보 출력
'''
if num == 0 :
    print("가위")
if num == 1 :
    print("바위")
if num == 2 : 
    print("보")
'''

if num == 0 :
    print("가위")
elif num == 1 :
    print("바위")
else : 
    print("보")