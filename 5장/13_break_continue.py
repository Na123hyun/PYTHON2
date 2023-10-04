'''
2023-10-04
컴퓨터공학부 202395004 김나현
반복하여 제어하는 break, continue
    교재 p137

    Test word : programming
'''

#사용자에게 단어를 입력 받는다.
word = input("단어를 입력하시오. : ")

#제목
print(":: break1 ::")

#for문
#i에 들어갈 단어는(a, e, i, o, u 중에 하나)
#or(또는)
#==(같다)
for i in word :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        #포함된 단어라면 반복을 종료
        #모음을 만나면 반복 중지
        break
    
    #포함되지 않은 단어라면 else
    # 결과 pr
    else :
        print(i, end ='')

print() #줄 바꿈

print(":: break2 ::")

for i in word :
    #i는 같다
    #리스트 형식
    #i == 'a'와 같다
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] : 
        #반복을 중단한다.
        #반복을 빠져나간다.
        break
    
    #포함되지 않은 단어라면 else
    # 결과 pr
    else :
        print(i, end ='')

print() #줄 바꿈

print(":: continue ::")

for i in word :
    #i는 같다
    #리스트 형식
    #i == 'a'와 같다
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
        #반복의 시작으로 돌아간다.
        #반복을 계속한다. 입력 받은 단어의 끝까지 결과를 출력한다.
        #모음을 만나면 그 모음은 print문을 만날 수 없다.(건너뛰다)
        continue
    
    #결과 예상
    #prgrmmng
    print(i, end ='')