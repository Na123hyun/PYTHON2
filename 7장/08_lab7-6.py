'''
2023-11-01
컴퓨터공학부 202395004 김나현
LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''

#다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

#최대, 최소 인구를 비교하기 위한 기준
#최대 인구 수 - 작은 수
max_population = 0

#최소 인구 수 - 큰 수 
min_population = 999999999999999999

#평균 인구 수
total_population = 0

#큰 도시는 없음, 비워둠
max_city = None

#작은 도시는 없음, 비워둠
min_city = None

#city에 city_info 저장
for city in city_info :
    #평균 인구 수와 1번지인 부산을 더해라
    total_population += city[1]

    #만약에, city_info의 1번지가 최대 인구 수보다 크다면,
    if city[1] > max_population :
        #최대 인구 수와 city_info의 1번지에 대입한다.
        max_population = city[1]
        #최대 도시를 city_info에 대입한다.
        max_city = city
    #만약에, city_info의 1번지가 최소 인구 수보다 크다면,
    if city[1] > min_population :
        #최소 인구 수와 city_info의 1번지에 대입한다.
        min_population = city[1]
        #최대 도시를 city_info에 대입한다.
        min_city = city

print("최대 인구 : {}, 인구 : {} 천명" .format(max_city[0], max_city[1]))
print("최소 인구 : {}, 인구 : {} 천명" .format(min_city[0], min_city[1]))
print("리스트 도시 평균 인구 : {} 천명" .format(total_population / len(city_info)))