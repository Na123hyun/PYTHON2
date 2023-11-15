'''
2023-11-15
컴퓨터공학부 202395004 김나현
문자열
'''

#문자열 슬라이싱
s = 'Happy Day!'

#0번지를 잘라서 보여줘
print(s[0])

#6번지부터 9번지까지
print(s[6:10])

#시작부터 뒤에서 -2번지 앞까지
print(s[:-2])

#줄 바꿈
print()

#문자열 분리 : split()
s = 'Welcome to Python'
#아무것도 안 적으면 공백을 기준으로 분리
print(s.split())

s = '2023.11.15'
#분리 기준은 .
print(s.split('.'))

s = 'Hello, world!'
#분리 기준은 , / 공백(문자열) 포함
print(s.split(','))

s = 'Hello, world!'
#분리 기준은 , 공백
print(s.split(', '))

#줄 바꿈
print()

#공백 제거 : strip()
s = 'Welcome, to, python, and, bla, bla     '
print(s.strip())
#쉼표 기준으로 분리(split())하고 x에 하나씩 담아서 공백을 제거(strip())하라
print([x.strip() for x in s.split(',')])

#리스트를 변환해서 출력. 쉼표와 문자열
print(list('Hello, World!'))

#줄 바꿈
print()

#문자열 연결 : join()
#,를 붙여서 연결하라
print(','.join(['apple', 'grape', 'banana']))

#.으로 구분된 번호를 -로 고친다
#.을 기준으로 분리해서 .을 -로 고친다
print('-'.join('010.1234.5678'.split('.')))

#.을 -로 바꾸기
print('010.1234.5678'.replace('.','-'))

#줄 바꿈
print()

s = 'Hello World!'
print(s)

#s에 저장된 문자열을 리스트로 문자열 분리 시켜 slist에 저장
slist = list(s)
print(slist)

#분리된 문자를 다시 합치기
#빈 공간 없이 합쳐줘
print(''.join(slist))

#줄 바꿈
print()

#줄 바꿈과 탭이 포함된 문자열 그대로 출력
#\n 줄 바꿈, \t 탭
a_string = 'Today as well, \n\t Have a Happy Day.'
print(a_string)

#문자열 자르기 word_list에 저장
#공백을 기준으로 분리, 줄 바꿈과 탭은 없다. 단어들 위주로만
word_list = a_string.split()
print(word_list)

#다시 합치기
#문자열을 자르고 다시 합치면 줄 바꿈과 탭이 삭제된다.
#단어들 위주로만 합친다.
refined_string = " ".join(word_list)
print(refined_string)

#줄 바꿈
print()

#대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s)
#lower() 전부다 소문자로 바꿈
print(s.lower())
#upper() 전부다 대문자로 바꿈
print(s.upper())

#공백 제거 strip()
s = '       Hello, World!        '
#왼쪽, 오른쪽 모든 공백을 제거
print(s.strip())
#왼쪽 공백 제거
print(s.lstrip())
#오른쪽 공백 제거
print(s.rstrip())

s = '#########Hello, World!#########'
print(s)
#제거
print(s.strip('#'))
#왼쪽 # 제거
print(s.lstrip('#'))
#오른쪽 # 제거
print(s.rstrip('#'))

#줄 바꿈
print()

#문자열 찾기
s = 'www.siila.ac.kr'

#.kr 찾기
#리스트, index(주소)
#12번지 .부터 kr까지
print(s.find('.kr'))

#-1 (문자열이 없다)
print(s.find('x'))

#. 개수
print(s.count('.'))