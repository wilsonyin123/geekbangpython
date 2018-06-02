# a * x + b = y

def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y


def a_line(a,b):
        return lambda x: a*x+b
    return arg_y


# a=3 b=5
# x=10 y=?
# x=20 y =?

# a=5 b=10

line1 = a_line(3, 5)
line2 = a_line(5,10)

print (line1(10))
print (line1(20))

#def func1( a,b, x)



