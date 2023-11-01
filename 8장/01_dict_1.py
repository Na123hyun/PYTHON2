'''
2023-11-01
컴퓨터공학부 202395004 김나현
8.1 키와 값을 가지는 딕셔너리
    튜플 = () 리스트 = [] 딕셔너리 = {}
'''

#빈 딕셔너리 생성
phone_book1 = {}

#딕셔너리에 값 저장. 1번 방법 : key, value [key] = value
phone_book1['김나현'] = '010-8282-5353'

print("phone_book1 : ", phone_book1)

#딕셔너리에 값 저장. 2번 방법 : {key : value}
phone_book2 = {'홍길동' : '010-7899-4545', '김나현' : '010-8282-5353'}
print("phone_book2 : ", phone_book2)

#줄 바꿈
print()

phone_book3 = {}
phone_book3['김나현'] = '010-2011-0421'
phone_book3['홍길동'] = '010-5678-1234'
phone_book3['정근우'] = '010-5268-1354'
phone_book3['이대호'] = '010-5853-2463'
phone_book3['신재영'] = '010-6335-9474'

print("phone_book3 ", phone_book3)

#줄 바꿈
print()

print(":: 전화번호 phone_book3 출력 ::")

#모든 key 출력
print(phone_book3.keys())

#모든 value 출력
print(phone_book3.values())

#모든 key, value 출력
print(phone_book3.items())

#줄 바꿈
print()

print(":: 전화번호 phone_book3 items() 출력 ::")

#key = name, value = phone_num
#한 눈에 볼 수 있겠끔 정리해서 출력된다.
for name, phone_num in phone_book3.items() :
    print(name, ":", phone_num)

#줄 바꿈
print()

print(":: 전화번호 phone_book3[keys]로 접근하여 출력 ::")

#key, 내 이름에 대한 value
for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])

#줄 바꿈
print()

print("딕셔너리 작성 시 :(콜론)을 기준으로 key : value 작성")
person_dict = {'name' : '김나현', 'age' : '18', 'class' : '1학년'}

#딕셔너리의 'name' 키로 값을 조회하여 출력
print("name :", person_dict['name'])
#딕셔너리의 'age' 키로 값을 조회하여 출력
print("나이 :", person_dict['age'])

#줄 바꿈
print()

print(":: 정렬 ::")
#phone_book3를 정렬
#딕셔너리의 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))

#줄 바꿈
print()

print(":: 키를 기준으로 전체 정렬 ::")
#lambda 이름이 없는 함수, 일회용으로 쓸 수 있는 함수
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)

#줄 바꿈
print()

print(":: 값을 기준으로 전체 정렬 ::")
#value의 값을 기준으로 정렬된다.
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

#줄 바꿈
print()

print(":: 항목 삭제 ::")
#del 삭제, key를 적으면 value도 같이 삭제된다.
del phone_book3['김나현']
print(phone_book3)

print(":: 전체 삭제 ::")
#key와 value 전체 삭제된다.
phone_book3.clear()
print(phone_book3)