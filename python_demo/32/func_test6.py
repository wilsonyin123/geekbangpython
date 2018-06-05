fd = open('name.txt')
try:
    for line in fd:
        print (line)
finally:
    fd.close()


with open('name.txt') as f:
    for line in f:
        print(line)
