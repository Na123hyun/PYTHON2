'''
2023-11-01
컴퓨터공학부 202395004 김나현
LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.

    08과 기준이 다르다.

'''

#다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

#최대, 최소 인구를 비교하기 위한 기준
#최대 인구 수 - 작은 수
#첫 번째 항목이 기준이다.
max_population = city_info[0][1]

#최소 인구 수 - 큰 수 
min_population = city_info[0][1]

#평균 인구 수
total_population = 0

#큰 도시는 없음, 비워둠
#첫 번째 항목이 기준이다.
max_city = city_info[0][0]

#작은 도시는 없음, 비워둠
#첫 번째 항목이 기준이다.
min_city = city_info[0][0]

#city에 city_info 저장
#도시명과 인구 수
for city, population in city_info :
    #평균 인구 수와 1번지인 부산을 더해라
    total_population += population
    #최대 인구 수와 1번지는 같다.
    if population > max_population :
        max_population = population
        max_city = city
    if population > min_population :
        min_population = population
        min_city = city

print("최대 인구 : {}, 인구 : {} 천명" .format(max_city, max_population))
print("최소 인구 : {}, 인구 : {} 천명" .format(min_city, min_population))
print("리스트 도시 평균 인구 : {} 천명" .format(total_population / len(city_info)))