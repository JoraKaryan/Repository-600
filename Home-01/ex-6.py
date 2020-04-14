#ex-6

a = int(input("number 1..."))
b = int(input("number 2..."))


def divisor(x,y):
    if y == 0:
        return x
    else:
        return divisor(y, x % y)
print(divisor(a,b))
