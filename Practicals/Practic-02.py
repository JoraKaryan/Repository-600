
#5

def foo(n):
    s=[x**2 for x in range(1,n+1)]
    d=0
    for i in s:
        d = d+i**2
    return d%10
print(foo(950))
