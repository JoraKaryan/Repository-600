#ex-1a

list_1 = [[1, 2], [1, 2], [1, 2, 3]]
cut_1 = [1, 2]


def remover(mylist, cut):
        while cut in mylist:
                mylist.remove(cut)
        return mylist
print(remover(list_1, cut_1))
