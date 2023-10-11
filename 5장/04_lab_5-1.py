'''
2023-09-27
컴퓨터공학부 202395004 김나현
터틀 그래픽으로 여러개의 원을 그려보자
'''

#turtle 함수 가져오기(포함시키기)
import turtle as t

#원 하나 그리기
#t.circle(100)

for count in range(10) :
    t.circle(100)
    t.left(360 / 10)
    #회전하는 각도

#종료
t.mainloop()
#t.done()