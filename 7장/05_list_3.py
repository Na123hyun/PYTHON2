'''
2023-10-18
202395004 컴퓨터공학부 김나현
리스트의 객체 생성과 참조
'''

fruits1 = ['딸기', '수박', '샤인머스켓']

#실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사된다.
#같은 곳을 참조한다.
fruits2 = fruits1

print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

#fruits2의 1번지 과일을 망고로 바꾸면
fruits2[1] = '망고'

#모두 1번지 내용이 망고로 바뀐다.
#주소를 참조하기 때문이다.(같은 주소)
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

#주소 확인 => 메모리 위치 정보 알아보기 id() 함수
#두 리스트의 id 정보가 같다.
print("fruits1의 id : ", id(fruits1))
print("fruits2의 id : ", id(fruits2))

#줄 바꿈
print()

'''
리스트 내용 복제하기 list() 함수
'''

#내용 복제(배정)
fruits2 = list(fruits1)
print(":: 내용 복제 후 1 ::")
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

print("fruits1의 id : ", id(fruits1))
print("fruits2의 id : ", id(fruits2))

#줄 바꿈
print()

#내용 복제 2
#처음부터 끝까지
fruits3 = fruits1[:]
print(":: 내용 복제 후 2 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)

#id 정보가 다르다
print("fruits1의 id : ", id(fruits1))
print("fruits3의 id : ", id(fruits3))

#줄 바꿈
print()

#0번지 내용을 수박으로 바꾼다.
fruits3[0] = '수박'
print(":: fruits3의 0번지에 수박으로 내용을 바꾼 후 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)
