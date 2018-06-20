# 练习一 字符串


```python
# 1. 定义一个字符串Hello Python 并使用print( )输出
string1 = 'Hello Python'
print(string1)


# 2. 定义第二个字符串Let‘s go并使用print( )输出

# 字符串内容包括单引号可以使用双引号将字符串括起来
string2 = "Let's go"
print(string2)


# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出

string3 = '"The Zen of Python" -- by Tim Peters'
print(string3)

```

# 练习二 字符串基本操作

```python
# 1. 定义两个字符串分别为 xyz 、abc
string1 = 'xyz'
string2 = 'abc'

# 2. 对两个字符串进行连接
# 字符串属于序列，序列连接操作符为“+”
print(string1 + string2)

# 3. 取出xyz字符串的第二个和第三个元素
# 序列的切片操作使用“[ ]”
print(string1[1])
print(string1[2])

# 4. 对abc输出10次
# 序列的重复操作
print(string2 * 10)

# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
# 判断字符是否存在于序列当中， 返回布尔值类型，如果存在返回True，不存在返回False
print('a' in string1)
print('a' in string2)
```


# 练习三 列表的基本操作

```python
# 1. 定义一个含有5个数字的列表
list1 = [5, 6, 7, 8, 9]
# 使用type( )可以查看变量的类型
print(type(list1))

# 2. 为列表增加一个元素 100
# 列表自带的方法很丰富，参考官方文档
# https://docs.python.org/3.5/library/stdtypes.html#sequence-types-list-tuple-range
list1.append(100)
print(list1)

# 3. 使用remove()删除一个元素后观察列表的变化
list1.remove(7)
print(list1)

# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(list1[0:3])
# 注意取出最后一个元素的类型为整型
print(list1[-1])

```





# 练习四 元组的基本操作

```python
# 1. 定义一个任意元组，对元组使用append() 查看错误信息
tuple1 = ('x', 'y', 3, 4, 5)
# 元组定义完成一般不可变，也没有append方法，会报错
# AttributeError: 'tuple' object has no attribute 'append'
# tuple1.append()

# 2. 访问元组中的倒数第二个元素
# 元组也是序列，因此可以使用序列操作
print(tuple1[-2])

# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
tuple2 = ('a', 'b', 'c')
print(tuple1 + tuple2)
# 组成新的元组之后会新申请一块内存存放元组，操作的两个元组不变
print(tuple1)
print(tuple2)

# 4. 计算元组元素个数
# 可以使用len( )方法计算，也可以使用自带的__len__( )方法得到元组元素的个数，
# 元组元素的个数和总长度是一样的
print(len(tuple1))
print(tuple1.__len__())
```


