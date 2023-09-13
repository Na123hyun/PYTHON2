'''
2023-09-13
김나현
'''

import turtle as t #터틀 모듈을 사용하기 위한 준비
                #turtle 클래스 객체를 t로 생성(별명)

t.shape('turtle')
t.speed(2) #속도가 느려짐

#선 그리기
'''
t.forward(200) #앞으로 200픽셀 이동
t.mainloop() #그림판 사라지지 않음
'''

'''
#삼각형 그리기
t.forward(200) #200픽셀 만큼 이동
t.left(120) #왼쪽으로 120도 회전
t.forward(200) #200픽셀 만큼 이동
t.left(120) #왼쪽으로 120도 회전
t.forward(200) #200픽셀 만큼 이동
t.left(120) #왼쪽으로 120도 회전
t.mainloop() #그림판 사라지지 않음
'''

for i in range(5) :
    t.forward(200) #200픽셀 만큼 이동
    t.left(144) #왼쪽으로 120도 회전
 
t.mainloop() #그림판 사라지지 않음