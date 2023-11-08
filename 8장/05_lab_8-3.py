'''
2023-11-8
컴퓨터공학부 202395004 김나현
p210 LAB 8-3
'''

#파티A와 파티B에 참석한 사람들의 명단
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])


#파티A와 파티B 둘다 참석한 사람 출력.
#교집합 메소드 intersection()
print("2개의 파티에 모두 참석한 사람은 다음과 같다.")
print(partyA.intersection(partyB))

#파티A와 파티B에 참석한 사람들을 중복되지 않도록 출력.
#합집합 메소드 union()
print(partyA.union(partyB))

#파티A와 파티B 중에서 한 군데만 참석한 사람 출력.
#대칭 차집합 메소드 symmetric_difference()
print(partyA.symmetric_difference(partyB))

#파티A에만 참석한 사람 출력.
#차집합 메소드 difference()
print(partyA.difference(partyB))