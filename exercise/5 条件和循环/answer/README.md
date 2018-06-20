# 练习一 条件语句的使用

```python
# 1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
string1 = '123456789'
# 使用len( )可以计算字符串的长度
print(len(string1))

# 判断相等可以使用“==”， 不相等可以使用 not 关键字
if not len(string1) == 10:
    print('字符串长度不为10')
else:
    print('字符串长度为10')

# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在
# 1-10，11-20，21-30，31-40，分别进行不同的输出
num_user_input = input('输入一个1-40之间的整数：')
num_to_int = int(num_user_input)
if 1 <= num_to_int <= 10:
    print('数字在1-10之间')
elif 11 <= num_to_int <= 20:
    print('数字在11-20之间')
elif 21 <= num_to_int <= 30:
    print('数字在21-30之间')
else:
    print('数字在31-40之间')
```


# 练习二 循环语句的使用

```python
# 1. 使用for语句输出1-100之间的所有偶数
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 2. 使用while语句输出1-100之间能够被3整除的数字
j = 1
while j <= 100:
    if j % 3 == 0:
        print(j)
    j += 1

```