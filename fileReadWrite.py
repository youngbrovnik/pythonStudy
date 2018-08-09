# fileReadWrite.py

# write
# f = open("newfile.txt", 'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# readline
f = open("newfile.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()

# readlines