# Opening Files in Python
'''
f = open('test.txt')  # open file in current directory
'''

# The default is reading in text mode. In this mode, we get strings when reading from the file.

'''
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
'''

# Original recommended syntax
# f = open("test.txt",'r', encoding='utf-8')
# closing a file
# f.close()
'''
# A Safer way is to use a try..finally block
try:
    f = open('test.txt', encoding='utf-8')
finally:
    f.close()
'''
# We don't need to explicitly call the close() method. It is done internally
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('This file\n')
    f.write('My first file\n')
    f.write("contains three lines\n")
# Reading Files in Python
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read(4))
    print(f.read(4))
    print(f.read())
    print(f.read())
    print(f.tell())
    print(f.seek(0))
    print(f.read())
    f.seek(0)
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.seek(0)
    for line in f:
        print(line, end='')
