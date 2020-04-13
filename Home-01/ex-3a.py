#ex-3a

string = input("type a word...")


def reverse_func(word):
    for_reverse = ""
    for i in range(1, len(word) + 1):
        reverse_index = len(word) - i
        for_reverse += word[reverse_index]
    return for_reverse

if string == reverse_func(string):
    print(True)
else:
    print(False)


