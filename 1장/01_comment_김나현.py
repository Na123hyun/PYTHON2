'''
2023-09-13
김나현
주석과 출력 함수 사용하기
'''

#학과 한번 이름을 저장하시오.
major = "컴퓨터공"
id = 202395004
name = '김나현'

#출력한다.
print("학과 : ", major) #변수를 쉼표로 구분해준다.
print("학번 : {}" .format(id))

#안녕하세요. 저는 00학과 00학번 00입니다.

print("안녕하세요. 저는 {}학부 {} {}입니다.".format(major,id,name)) #위치 순서대로 맞추기
print("안녕하세요. 저는 ", major, "학과 ", id, "학번 ", name ," 입니다.")

#파이썬을 10개 출력하시오. (반복문 사용 안 함)
print("파이썬" * 10)

num1 = '10' 
num2 = '20'

print(num1 + num2)
