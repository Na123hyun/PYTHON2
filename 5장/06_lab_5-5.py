'''
2023-09-27
컴퓨터공학부 202395004 김나현
반복문으로 팩토리얼 구하기
'''

#정수 입력 받기
num = int(input("정수를 입력하시오. : "))
#초기값은 1
fact = 1

#반복문(for)
for i in range(1, num + 1) :
    fact = fact * 1

#결과 출력
print(num, "!은", fact, "이다.")