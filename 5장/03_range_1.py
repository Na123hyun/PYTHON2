'''
2023-09-27
컴퓨터공학부 202395004 김나현
range() 함수
'''

#i 변수에 0 ~ 2의 값이 저장됨
for i in range(3) :
    print(i, end = '. ')
    #end = ' '로 지정하면 줄 바꿈하지 않는다. 
    print("안녕하세요.")
    print("   김나현입니다.")
    #print가 줄 바꿈까지 포함되어 있다.

print() #줄 바꿈

#range(시작값, 숫자 앞까지 증가값(감소값))
#C언어 -> for(초기값; 조건식; 증감식) / range()는 ;(세미콜론)
#range(1, 6, 1)
for i in range(1, 6) :
    print(i, end = ' ')

print() #줄 바꿈

#10 ~ 1까지 출력
#감소값은 명시해줘야 한다.
for i in range(10, 0, -1) :
    print(i, end = ' ')