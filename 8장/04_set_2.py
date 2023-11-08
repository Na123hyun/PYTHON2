'''
2023-11-8
컴퓨터공학부 202395004 김나현
집합의 연산
'''

#비교 연산자
num1 = {1, 2, 3}
num2 = {1, 2, 3}
print("num1 == num2?", num1 == num2)

#6개의 숫자로 집합 생성
num_set = {1, 3, 4, 5, 2, 6, 4}
print("num_set : ", num_set)
print("num_set 길이 : ", len(num_set))
print("num_set 최대값 : ", max(num_set))
print("num_set 최소값 : ", min(num_set))
print("num_set 합계 : ", sum(num_set))

#줄 바꿈
print()

num1 = {1, 2, 3}
num2 = {3, 4, 5}

#합집합
#합집합 연산자 |
#중복을 포함하지 않는다.
print("num1 | num2 : ", num1 | num2)

#합집합 메소드 union()
print("num1.union(num2) : ", num1.union(num2))

#교집합
#교집합 연산자 &
#교집합 메소드 intersection()
print("num1.intersection(num2) : ", num1.intersection(num2))

#차집합
#차집합 연산자 -
#차집합 메소드 difference()
print("num1.difference : ", num1.difference(num2))

#대칭 차집합
#대칭 차집합 연산자 ^
#대칭 차집합 메소드 symmetric_difference()
print("num1.symmetric_difference : ", num1.symmetric_difference(num2))