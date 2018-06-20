# 练习一 字典的使用

```python
# 1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
dict1 = {'a': 'aa', 'b': 'xyz', 'c': 'Helo', 'd': 123}

# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
# 字典的key不能重复，否则会覆盖掉相同key的值
dict1['c'] = 'cake'
print(dict1)

# 3. 取出字典中关键字为d的值
print(dict1['d'])
```

# 练习二 集合的使用

```python
# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str1 = 'hello'
# 集合里的元素不能重复
print(set(str1))

```