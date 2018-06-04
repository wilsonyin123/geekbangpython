# # 练习一 字符串
#
# 1. 定义一个字符串Hello Python 并使用print( )输出

str1 = 'Hello Python!'

print(str1)

# 2. 定义第二个字符串Let‘s go并使用print( )输出

str2 = "Let's go"

print(str2)

# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出

str3 = " \"The Zen of Python\" -- by Tim Peters"

print(str3)



# # 练习二 字符串基本操作
#
# 1. 定义两个字符串分别为 xyz 、abc

str_a = 'xyz'
str_b = 'abc'

# 2. 对两个字符串进行连接

print(str_a + str_b)

# 3. 取出xyz字符串的第二个和第三个元素

print('xyz字符串的第二个元素是 %s ' % str_a[1])
print('xyz字符串的第三个元素是 %s ' % str_a[2:])

# 4. 对abc输出10次

for i in range(10) :
    print('输出 %s 第 %i 次' %(str_b,i+1))

# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

if 'a' in str_a :
    print('a字符（串）在 xyz ')
elif 'a' in str_b :
    print('a字符（串）在 abc ')

# # 练习三 列表的基本操作
#
# 1.定义一个含有5个数字的列表

a_list = [1,2,3,4,5]

print(a_list)

#
# 2.为列表增加一个元素
# 100

a_list.append(100)

print(a_list)

#
# 3.使用remove() 删除一个元素后观察列表的变化

a_list.remove(1)

print(a_list)

#
# 4.使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

print('列表的前三个元素',a_list[:3])
print('列表的最后一个元素',a_list[-1])