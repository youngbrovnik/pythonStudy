# fileReadWrite.py

# write
def write():
    f = open("newfile.txt", 'w')
    for i in range(1,11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

# write()

# readline
def readline():
    f = open("newfile.txt", 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line, end='')
    f.close()

# readline()

# readlines
def readlines():
    f = open("newfile.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()

# readlines()

# read
def read():
    f = open("newfile.txt", 'r')
    data = f.read()
    print(data)
    f.close()

# read()

# adddata
def adddata():
    f = open("newfile.txt", 'a')
    for i in range(11,20):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

# adddata()

# with
def withtest():
    with open("newfile.txt", 'r') as f:
        data = f.read()
        print(data)

# withtest()
