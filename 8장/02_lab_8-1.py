'''
2023-11-01
컴퓨터공학부 202395004 김나현
LAB 8-1 편의점 재고 관리 프로그램
'''

items = {"커피음료" : 7, "펜" : 3, "종이컵" : 2, "우유" : 1, "콜라" : 4, "책" : 5}

#물건의 목록을 출력한다.
#print(items.keys())
print("제품 목록 : ", end=' ')
for key in items.keys() :
    print(key, end=', ')

#줄 바꿈
print()

#물건의 이름을 입력받아 재고를 출력한다.
name = input("물건의 이름을 입력하십시오. : ")
print("재고 : ", items[name])