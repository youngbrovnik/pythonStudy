# [문제1] 홀수 짝수 판별
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.
def is_odd(num):
    if num%2==0:
        return "짝수입니다."
    else:
        return "홀수입니다."

# [문제2] 평균값 계산
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)
def ave(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)


# [문제3] 구구단 출력
# 입력을 자연수 n(2부터 9까지의 자연수)으로 받았을 때, n에 해당되는 구구단을 출력하는 함수를 작성해 보자.
def roMulti(times):
    for i in range(9):
        print(times, "x", i+1, "=", times*(i+1))
'''
[문제4] 피보나치
입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
피보나치 수열은 다음과 같은 순서로 결과값을 리턴한다.
fib(0) → 0 리턴
fib(1) → 1 리턴
fib(2) → fib(0) + fib(1) → 0 + 1 → 1 리턴
fib(3) → fib(1) + fib(2) → 1 + 1 → 2 리턴
fib(4) → fib(2) + fib(3) → 1 + 2 → 3 리턴
'''
def fibo(num):
    fibo_arr = [0,1,1]
    if num <= 2:
        return fibo_arr[num]
    else:
        for i in range(num-2):
            fibo_arr.append(fibo_arr[i+1]+fibo_arr[i+2])
    return fibo_arr[num]

'''
[문제5] 5보다 큰 수만
다음은 숫자들로 이루어진 리스트를 입력으로 받아 5보다 큰 수만 필터링하여 리턴해 주는 함수이다.
>>> def myfunc(numbers):
...     result = []
...     for number in numbers:
...         if number > 5:
...             result.append(number)
...     return result
... 
>>> myfunc([2,3,4,5,6,7,8])
[6, 7, 8]
위 함수를 lambda 함수로 변경해 보시오.
'''

#lambda
numbers = [2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x > 5, numbers))
print(result)
