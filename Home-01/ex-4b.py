#ex-4b

num = int(input("type a number"))

def foo(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s
print (foo(num))


