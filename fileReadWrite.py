# fileReadWrite.py

# write
def write():
    f = open("data/newfile.txt", 'w')
    for i in range(1,11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

# write()

# readline
def readline():
    f = open("data/newfile.txt", 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line, end='')
    f.close()

# readline()

# readlines
def readlines():
    f = open("data/newfile.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()

# readlines()

# read
def read():
    f = open("data/newfile.txt", 'r')
    data = f.read()
    print(data)
    f.close()

# read()

# adddata
def adddata():
    f = open("data/newfile.txt", 'a')
    for i in range(11,20):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

# adddata()

# with
def withtest():
    with open("data/newfile.txt", 'r') as f:
        data = f.read()
        print(data)

# withtest()
