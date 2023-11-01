'''
2023-10-18
202395004 컴퓨터공학부 김나현
도시의 인구 자료에 대한 슬라이싱하기
'''

#서울, 부산, 인천 인구의 리스트 생성
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

#서울 인구의 2번지를 출력한다.
#population = ["Seoul"(0번지), 9765(1번지), "Busan"(2번지), 3441(3번지), "Incheon"(4번지), 2954(5번지)]
print("서울 인구 : ", population[1])

#인천 인구의 마지막을 출력한다.
#인덱스 음수를 사용한다. => -1은 5번지
print("인천 인구 : ", population[-1])

#도시 리스트의 처음부터 2씩 증가하면서 출력한다.
#0번지, 2번지, 4번지
cities = population[0::2]
print("도시 리스트 : ", cities)

#마지막까지 인구 수의 합을 출력한다.
#sum() 함수 사용.
pops = population[1::2]
print("인구의 합 : ", sum(pops))