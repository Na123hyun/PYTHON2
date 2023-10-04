'''
2023-10-04
컴퓨터공학부 202395004 김나현
조건에 따라 반복문으로 while문
    교재 p127
'''

#while 조건식 : -> :(콜론) 반드시 사용
#   들여쓰기로 반복하면서 할 일 작성

#반복문에서는 반드시 종료 조건이 있어야 한다.
#while True : -> 무한 반복


#공사중
under_construction = True

#True일 동안 계속 반복 (무한 반복)
while under_construction :
    response = input("공사가 완료 되었습니까? : ")

    #종료 조건
    if response == "예" :

        #공사 완료
        under_construction = False
        #False = break(반복 종료)

print("루프 탈출!")