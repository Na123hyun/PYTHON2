'''
2023-11-15
컴퓨터공학부 202395004 김나현
LAB 9-2 : 트위터 메세지 처리의 단어 추출
    띄어쓰기로 문자열을 분리하고, 단어의 개수 찾기
'''

text1 = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
        It's because when we show up, things change."

#띄어쓰기로 문자열을 분리하고, 단어의 개수 찾기
#len() => 길이(개수) : 리스트의 항목 개수 찾는 함수
text2 = text1.split()
print(text2)
print('Woredl count : ', len(text2))

#줄 바꿈
print()

#도전문제 9.1
#회사 이름은 **로 표시
#kT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
    Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'

#소문자 변환
low_text = text.lower()

#1
#모든 문자를 소문자로 변환
#소문자로 바뀐 단어들을 공백으로 구분한다.
#구분된 단어를 검사한다. (판단) => 단어가 kt 또는 samsung 또는 lg 또는 skt인가?
#검사한 단어가 회사명이면 **로 바꾼다.
#아니면 그 단어는 그대로 사용한다.
#결과 출력

text = ''
for word in low_text.split(' ') :
    if word == 'kt' or word == 'samsung' or word == ' lg' or word == 'skt' :
        text += '** '
    else :
        text += word + ' '
print('text1 : ', text)

#줄 바꿈
print()

#2.
#소문자로 바뀐 단어들을 공백으로 구분한다.
#리스트에 저장된 단어를 검사한다. (판단) => 단어가 kt 또는 samsung 또는 lg 또는 skt인가?
#검사한 단어가 회사명이면 **로 바꾸어 리스트에 저장한다.
#아니면 그 단어는 그대로 리스트에 저장한다.
#분리된 단어들을 합친다.
#결과 출력

split_text = low_text.split(' ')
text = ''
for word in low_text.split(' ') :
    if word == 'kt' or word == 'samsung' or word == ' lg' or word == 'skt' :
        text += word.replace(word, '** ')
    else :
        text += word + ' '
print('text2 : ', ''.join(text))
