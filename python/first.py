import os
import sys
import pickle

print(sys.platform)
print(sys.api_version)
# print(sys.copyright)


print(os.getcwd())

x = 'spam'
print(x * 10)

myfile=open('myfile.txt', 'w')
myfile.write('hello world test\n')
myfile.write('goodbye world\n')
myfile.close()

# myfile = open('myfile.txt')
# myfile.readline()
# myfile.readline()
# myfile.readline()

for line in open('myfile.txt'):
    print('===============')
    print(line, end='')


D = {'a':1, 'b':2}
F = open('myfile2.obj', 'wb')  #wb写入二进制模式
pickle.dump(D, F)
F.close()

G = open('myfile2.obj', 'rb')
E = pickle.load(G)
print(E)