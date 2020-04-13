#ex-4a

num = int(input("type a number"))

num_change = list(str(num))

x = 0
for i in num_change:
    x = x + int(i)
print(x)
