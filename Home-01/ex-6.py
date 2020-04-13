#ex-6
#Recursiaov chstaca

a = int(input(" ..."))
b = int(input(" ..."))

c = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        c.append(i)
print(c[-1])
