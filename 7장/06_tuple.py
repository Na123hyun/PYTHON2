'''
2023-11-01
컴퓨터공학부 202395004 김나현
한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''

#리스트 생성
color_list = ['red', 'blue', 'green', 'orange']

#튜플 생성
color = ('red', 'blue', 'green', 'orange')

#튜플 출력
print(f"color : {color}")

#color에 black 추가하기
#AttributeError: 'tuple' object has no attribute 'append'
#AttributeError: 'tuple' 개체에 'append' 속성이 없습니다
#튜플은 추가, 삭제가 안 된다.
#color.append('black')

#줄바꿈
print()

#인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print("color 튜플 : ",color)

#1번지부터 4번지 앞에까지
print("color 튜플 중 2, 3, 4번은? ", color[1:4])

#0번지부터 3번지 앞까지
print("color 튜플 중 1, 2, 3번은? ", color[0:3])

#시작값을 안 적어도 처음부터 시작
print("color 튜플 중 1, 2, 3번은? ", color[:3])

#2번지부터 마지막까지
print("color 튜플 중 3번 ~ 끝은? ", color[2:])

#시작부터 끝까지 2씩 증가
print("color 튜플 중 1, 3, 5번은? ", color[::2])

#거꾸로 출력 - 4번지부터 0번지까지
print("color 튜플 거꾸로 출력 ", color[::-1])

#줄바꿈
print()

#튜플 끼리의 결합 => + 연산자, 반복 => * 연산자
colors = color + color
print("colors 튜플 : ", colors)

#줄바꿈
print()

print("color 튜플을 10번 반복 : ", color * 10)