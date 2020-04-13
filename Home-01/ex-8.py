#ex-8

mylist = [4,2,1]


def foo(l):
    for i in range(1,len(l)+1):
        if len(l) == max(l):
            return max(l)+1
        if i not in l:
            return i
    if len(l) == 0:
        return 1
print(foo(mylist))
