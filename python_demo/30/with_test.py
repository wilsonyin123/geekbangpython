class Testwith(object):
    '''
    with 包含了 __enter__ 和 __exit__ 方法
    '''

    def __enter__(self):
        print('run now ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit normal ')
        else:
            print('exit with exception')


with Testwith():
    print('test')
    raise NameError('Exception')