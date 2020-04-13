#ex-2b

mylist = [44, [5, 6], 4, [2, 58, 1], [5, 6], [5, 6], 4, 4, 4, 6]

del_dupl = []
x = [del_dupl.append(mylist[i]) for i in range(len(mylist)) if mylist[i] not in del_dupl]
print(del_dupl)
