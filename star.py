#star.py

# i,j = 0,0
# while i<4:
#     i+=1
#     j=0
#     while j<i:
#         print('*', end='')
#         # print("i: %d" % i)
#         # print("j: %d" % j)
#         j+=1
#     print()

i=0
while i<4:
    i+=1
    print('*'*i, end='')
    print()


print()
while i>0:
    print(" "*(4-i), end='')
    print(('*'*(i*2-1)))
    i-=1

