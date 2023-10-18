'''
2023-10-18
202395004 컴퓨터공학부 김나현
리스트에서 사용 가능한 함수
'''
#리스트 생성
num_list = [1,2,3,4,5,6,7,8,9]


print("num_list : ", num_list)

#len(무엇을 할 것인지 넣는다.)
print("num_list 길이 : ", len(num_list))

#max()
print("num_list 최대값 : ", max(num_list))

#min()
print("num_list 최소값 : ", min(num_list))

#sum()
print("num_list 합계 : ", sum(num_list))

#sum() / len()
print("num_list 평균 : ", sum(num_list) / len(num_list))

#any()
print("num_list 항목 중 0이 아닌 원소가 있는 가? : ", any(num_list))