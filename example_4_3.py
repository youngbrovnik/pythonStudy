'''
[문제1] 파일 읽고 출력하기

다음은 "test.txt"라는 파일에 "Life is too short" 라는 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())
이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정하시오.
'''

'''
[문제2] 파일저장

사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성하시오. (단, 프로그램을 다시 실행하더라도 기존 작성한 내용을 유지하고 새로 입력한 내용이 추가되어야 한다.)

다음은 실행 예제이다.

저장할 내용을 입력하세요:
실행 할 때마다 사용자가 입력한 내용이 test.txt파일에 추가되어야 한다.
'''

'''
[문제3] 역순 저장

다음과 같은 내용의 파일 abc.txt가 있다.

abc.txt

AAA
BBB
CCC
DDD
EEE
이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

EEE
DDD
CCC
BBB
AAA
'''

'''
[문제4] 파일 수정

다음과 같은 내용을 지닌 파일 test.txt 가 있다.

test.txt

Life is too short
you need java
이 파일의 내용중 java라는 문자열을 python으로 바꾸어서 저장하시오.
'''

'''
[문제5] 평균값 구하기

다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.

sample.txt

70
60
55
75
95
90
80
80
85
100
sample.txt 파일의 숫자값을 모두 읽어 총합과 평균값을 구한 후 평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해 보자.
'''
