
# 读取人物名称
f = open('name.txt')
data = f.read()
data0 = data.split('|')

# 读取兵器名称
f2 = open('weapon.txt')
# data2 = f2.read()
i = 1
for  line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1

f3 = open('sanguo.txt',encoding='GB18030')
print(f3.read().replace('\n',''))
#
#
# def func(filename):
#     print(open(filename).read())
#     print('test func')
#
#
#
# func('name.txt')
