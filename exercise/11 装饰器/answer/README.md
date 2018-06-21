# 练习一 定义装饰器，用于打印函数执行的时间
1. 统计函数开始执行和结束执行的时间
2. 扩展练习：为装饰器传入超时时间，函数执行超过指定时间后退出
```python
# 为装饰器传入超时时间，函数执行超过指定时间后退出
# windows下signal.SIGALRM不可用

import time
import signal


def timeout(seconds=10, error_message="Timer expired"):
    def decorator(func):
        def handler(singnum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator


@timeout(5)
def getinfo(msg):
    print("getinfo start!")
    print("msg: %s" % msg)
    time.sleep(10)
    print("getinfo end!")
    return 1


if __name__ == '__main__':
    try:
        getinfo('Test!')
    except TimeoutError as e:
        print("time out: %s" % e)

```


# 练习二 定义装饰器，实现不同颜色显示执行结果的功能
```python
# 1. 向装饰器传递参数，通过传递的参数获取到输出的颜色
# 2. 被装饰函数的print( )输出根据装饰器得到的颜色进行输出
import sys


def make_color(code):
    def decorator(func):
        def color_func(s):
            if not sys.stdout.isatty():
                return func(s)
            tpl = '\x1b[{}m{}\x1b[0m'
            return tpl.format(code, func(s))
        return color_func
    return decorator


@make_color(33)
def fmta(s):
    return '{:^7}'.format(str(float(s) * 1000)[:5] + 'ms')

```