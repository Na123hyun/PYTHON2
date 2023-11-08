'''
2023-11-8
컴퓨터공학부 202395004 김나현
심화문제 8.3
    1. 3명의 학생 학번, 이름, 전화번호의 3쌍의 요소를 가지는
    student_tuple라는 튜플이 존재한다.

    2. 이 튜플을 수정하여 {학번 : [이름, 전회번호]}의 쌍으로
    이루어진 딕셔너리를 만들어 출력하시오.
        (반복문 활용)

    3. 이 정보를 이용하여 학생의 학번을 입력 받아
    이름과 전화번호를 출력하는 학사정보 프로그램을 작성.

    4. student_tuple의 마지막 항목으로 학점을 추가한다.
        이 정보를 바탕으로 딕셔너리를 만들어 출력.

    5. 학생의 학점 평균을 출력.
'''

student_tuple = [('202395001', '일길동', '010-8282-5353'), ('202395002', '이길동', '010-0235-5667'), ('202395003', '삼길동', '010-8382-5423')]

student_dict = {}
#1. 딕셔너리에 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name, phone]

#2. 딕셔너리 내용 출력
for  key, value in student_dict.items() :
    print(key, " : ", value)

#3. 학번을 입력 받아 이름과 연락처 출력
number = input("학번을 입력하시오. : ")
print("이름 : ", student_dict[number][0])
print("연락처 : ", student_dict[number][1])

#4. student_tuple의 마지막 항목으로 학점을 추가
student_dict['202395001'].append(4.5)
student_dict['202395002'].append(3.8)
student_dict['202395003'].append(3.5)

for  key, value in student_dict.items() :
    print(key, " : ", value)

#5. 학생의 학점 평균을 출력한다.
print("전체 학생의 학점 평균 : ")
sum = 0
for key, value in student_dict.items() :
    sum = sum + value[2]
#.2f는 소수점 2자리 출력
print(f"평균 : {(sum/3):.2f}")