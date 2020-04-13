#ex-2g

mylist = [44, [5, 6], 4, [2, 58, 1], [5, 6], [5, 6], 4, 4, 4, 6]
del_dupl = []


def foo(l,new):
    x = [new.append(l[i]) for i in range(len(l)) if l[i] not in new]
    return new

print(foo(mylist,del_dupl))
