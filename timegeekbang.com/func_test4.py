import time

# print( time.time())

def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间是 %s 秒 " % (stop_time - start_time))
    return wrapper



@timmer
def i_can_sleep():
    time.sleep(3)




# start_time = time.time()
i_can_sleep()

# stop_time = time.time()

# print('函数运行了 %s 秒' %(stop_time-start_time))
