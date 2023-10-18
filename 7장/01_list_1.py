'''
2023-10-18
202395004 컴퓨터공학부 김나현
리스트 만들기
'''

#과일 리스트 만들기
fruits = ['사과', '배', '샤인머스켓']
print("과일 목록 : ", fruits)

#수박 추가  => append() 메소드 사용 - 마지막에 추가된다.
fruits.append('수박')
print("과일 목록(수박 추가) : ", fruits)

fruits.append('망고')
print("과일 목록(망고 추가) : ", fruits)

#포도 추가 => + 연산자 사용 - 연결 연산자
#포도를 더해서 fruits에 저장, num = num + 1
fruits = fruits + ['포도']
print("과일 목록(포도 추가) : ", fruits)

#리스트에서 + 는 연결이다.
num = [1,2,3] + [4,5,6]
print("숫자 리스트 : ", num)

#* 연산자 - 리스트를 n번 반복한다.
num = [1,2,3] * 3
print("숫자 리스트 * 3 : ", num)

#in 연산자 => 포함되는 가?
print("과일 목록에 망고가 있나요? : ", '망고' in fruits)

#줄 바꿈
print()

'''
인덱스를 사용하여 리스트의 항목에 접근하기 p178
'''
#과일 리스트에 있는 과일의 개수?
print("과일 리스트에 있는 과일 개수는? : ",len(fruits))

#과일 리스트 중 제일 첫 번째 과일은?
print("과일 중 제일 좋아하는 과일은? : ", fruits[0])

#과일 리스트 중 제일 마지막 과일은?
print("과일 중 제일 마지막 과일은? : ", fruits[-1])

#과일 중 가장 큰 과일은?
print("과일 중 가장 큰 과일은?(사전식 순서) : ", max(fruits))

#과일 중 가장 작은 과일은?
print("과일 중 가장 작은 과일은?(사전식 순서) : ", min(fruits))

#정렬
#오름차순
fruits.sort()
print("오름차순 정렬 : ", fruits)

#내림차순
fruits.sort(reverse=True)
print("내림차순 정렬 : ", fruits)

#줄 바꿈
print()

'''
리스트를 원하는 모양으로 자르는 슬라이싱
'''

print("과일 목록 : ", fruits)

#1번지 ~ 4번지 앞까지
print("과일 리스트 중 2, 3, 4번 과일은? : ", fruits[1:4])

#0번지 ~ 2번지 앞까지
print("과일 리스트 중 1~3번 과일은? : ", fruits[0:3])

#콜론 앞에 아무것도 안 적으면 처음부터
#처음부터 2번 앞까지
print("과일 리스트 중 1~3번 과일은? : ", fruits[:3])

#콜론 뒤에 아무것도 안 적으면 마지막까지
#2번지부터 마지막까지
print("과일 리스트 중 3번 과일부터 마지막까지 과일은? : ", fruits[2:])

#처음부터 끝까지 리스트 중에서 2씩 증가하면서
print("과일 리스트 중 1, 3, 5번 과일은? : ", fruits[::2])

#기존의 리스트를 역순으로 출력
print("과일을 거꾸로 출력 : ", fruits[::-1])

#줄 바꿈
print()

'''
리스트의 원소 값을 자유롭게 조작해보자
'''

print("과일 목록 : ", fruits)

#원하는 위치에 '두리안' 추가 => insert() 메소드
fruits.insert(3, '두리안')
print("과일 목록(3번지에 두리안 추가) : ", fruits)

#위치 찾기 => index() 메소드
print("사과의 위치는? ", fruits.index('사과'))

#사과를 마지막에 추가
fruits.append('사과')
print("과일 목록(마지막에 사과 추가) : ", fruits)

#사과의 개수 => count() 메소드
print("사과의 개수는? : ", fruits.count('사과'))

#줄 바꿈
print()

'''
리스트의 항목 삭제
'''

#사과 삭제 => remove() 메소드 - 삭제할 항목을 지정
#처음 만난 사과만 삭제
fruits.remove('사과')
print("과일 목록(사과 삭제 후) : ", fruits)

#항목 삭제 => pop() 메소드
#마지막 항목을 삭제 - 무조건
fruits.pop()
print("과일 목록(마지막 과일 삭제) : ", fruits)

#del() 키워드 => 포도 삭제
#0번지 항목 삭제
del fruits[0]
print("과일 목록(포도(0번지) 삭제) : ", fruits)
