'''
2023-11-8
컴퓨터공학부 202395004 김나현
심화문제 8.6
'''

#튜플의 요소로 학번, 이름, 전화번호
student_tuple = [('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'), ('211103', '김수정', '010-123-3333')]

#빈 집합 생성
student_dict = {}

#딕셔너리에 추가
for number, name, phone in student_tuple :
    student_dict[number] = [name, phone]

#딕셔너리 내용 출력
for  key, value in student_dict.items() :
    print(key, " : ", value[0])

#학생에게 학번을 입력 받고 입력 받은 학생의 정보(이름, 전화번호)를 출력.
#이름은 0번지, 전화번호는 1번지
number = input("학번을 입력하시오. : ")
print(number + ' 학생은 ' + student_dict[number][0] + '이며, 전호번호는 ' +  student_dict[number][1] + '입니다.')