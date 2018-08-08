'''
[문제1] 두 수의 합은?
다음은 두 개의 숫자를 입력받아 더하여 리턴해 주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
이 프로그램을 수행 해 보자.

첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결과가 리턴되었다. 이 프로그램의 오류를 수정하시오.
'''
def sum():
    input1 = input("첫번째 숫자를 입력하세요: ")
    input2 = input("두번째 숫자를 입력하세요: ")
    total = int(input1) + int(input2)
    print("두 수의 합은 %s 입니다" % total)

# sum()

'''
[문제2] 숫자의 총합
사용자로부터 다음과 같은 숫자들의 입력을 받아 입력받은 숫자들의 총합을 구하는 프로그램을 작성하시오. (단, 숫자들은 콤마로 구분하여 입력한다.)
65, 45, 2, 3, 45, 8
'''

def sumInput():
    inputArr = input("숫자 입력: ").split(',')
    
    # print(inputArr)
    sum = 0
    for i in inputArr:
        sum += int(i)
    print("입력받은 숫자의 총합은 : %d " % sum)

# sumInput()

# [문제3] 문자열 출력
# 다음 중 출력결과가 다른 것 한개를 고르시오.

# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you", "need", "python")
# print("".join(["you", "need", "python"]))

#3번.

'''
[문제4] 한줄 구구단

사용자로부터 2~9 까지의 숫자중 하나를 입력받아 해당 숫자의 구구단을 한줄로 출력하는 프로그램을 작성하시오.

실행 예

구구단을 출력할 숫자를 입력하세요(2~9): 2
2 4 6 8 10 12 14 16 18
'''

def oneLineGugudan():
    n = input('구구단을 출력할 숫자를 입력하세요(2~9): ')
    for i in range(1, 10):
        print(int(n)*int(i), end=' ')
    print()

# oneLineGugudan()


