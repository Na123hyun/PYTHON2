'''
2023-10-18
202395004 컴퓨터공학부 김나현
입력을 받아 맛있는 과일 리스트를 만들자

    좋아하는 과일 5개를 입력 받아 리스트에 저장한다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는 지 없는 지 판단한다.

    추가 = append() 메소드
    찾기 = in 연산자
'''

#빈 리스트 생성
fruits = []

#5번 반복하면서 과일 이름 입력 받아 리스트에 저장
for i in range(5) :
    #str을 문자열로 변환
    name = input(str(i+1) + ". 좋아하는 과일의 이름을 입력하시오. : ")
    #입력 받은 변수의 값을 리스트에 추가
    fruits.append(name)
print("입력한 과일 리스트 : ", fruits)

'''
for i in range(5) :
    fruits.append(input("좋아하는 과일의 이름을 입력하시오. : "))
print("내가 좋아하느 과일 리스트 출력 : ", fruits)
'''

#찾기
favo_fruit = input("좋아하는 과일 하나를 입력하시오. : ")

#사용자가 입력한 과일이 리스트에 있는 지 판단.
#있으면 => 00은 당신이 좋아하는 과일입니다.
#없으면 => 00은 당신이 좋아하는 과일이 아닙니다..
if favo_fruit in fruits :
    print("{}은(는) 당신이 좋아하는 과일입니다.".format(favo_fruit))
else :
    print("{}은(는) 당신이 좋아하는 과일이 아닙니다.".format(favo_fruit))
