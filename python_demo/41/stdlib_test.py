# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__


# . ^ $ * + ? {m} {m,n} [] |  \d \D \s ()
# ^$
# .*?

import re


p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print (p.match('aa2018-05-10bb').group(2) )
# print (p.match('2018-05-10').groups() )
#
# year, month, day = p.match('2018-05-10').groups()
# print(year)
#
# print (p.search('aa2018-05-10bb'))
# phone = '123-456-789 # 这是电话号码'
# p2 = re.sub(r'#.*$','',phone)
# print(p2)
# p3 = re.sub(r'\D','',p2)
# print(p3)
# findall()

import  random
print( random.randint(1,5))
print( random.choice(['aa','bb','cc']))