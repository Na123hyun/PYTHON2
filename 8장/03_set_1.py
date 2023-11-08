'''
2023-11-8
컴퓨터공학부 202395004 김나현
집합 set()
'''
#빈 집합 생성
number = set()

#숫자 3개로 이루어진 집합
#{} 안에 나열되어 있다 - > 집합
number1 = {2, 1, 3}
print("number1 : ", number1)

#리스트로부터 집합 생성
#중복을 허용하지 않는다.
number2 = set([1, 2, 3, 1, 2])
print("number2 : ", number2)

#문자열을 집합으로 생성
text1 = set("asdfasdf")
print("text1 : ", text1)

numbers = {2, 4, 5, 1, 2}
#집합 안에 1이 있는 가?
#in = 포함되어 있는 가?
if 1 in numbers :
    print("집합에 1이 있습니다.")

#집합은 순서가 없어서 index로 접근이 불가능하다.
#반복문으로 접근하여 출력 가능하다.
numbers = {3, 4, 5, 1, 3, 4, 6}
#for는 numbers 안에
for num in numbers :
    print(num, end = ' ' )

#정렬 후 출력하기
#실제로 정렬을 하려면 sort()를 사용해야 한다.
for num in sorted(numbers) :
    print(num, end = ' ' )

#줄 바꿈
print()

#추가하기
numbers.add(100)
for num in sorted(numbers) :
    print(num, end='')

#줄 바꿈
print()

#삭제하기
numbers.remove(100)
print(num, end='')