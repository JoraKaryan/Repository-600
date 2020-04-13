#ex-5

num = int(input(" ..."))

binar = (bin(num)[2:])
x = 0
for i in binar:
    x = x + int(i)
print(x)
