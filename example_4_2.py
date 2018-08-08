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
# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)

'''
[문제2] 숫자의 총합
사용자로부터 다음과 같은 숫자들의 입력을 받아 입력받은 숫자들의 총합을 구하는 프로그램을 작성하시오. (단, 숫자들은 콤마로 구분하여 입력한다.)
65, 45, 2, 3, 45, 8
'''

def sumInput():
    inputArr = input("숫자를 입력하세요")
    
    # print(inputArr)
    sum = 0
    for i in inputArr:
        sum += int(i)
    print("입력받은 숫자의 총합은 : %d " % sum)

sumInput()