#ex-7

bar = "What is this book about? this book is about python coding"

if "?" in bar:
    bar = bar.replace('?', "")
l = bar.split(" ")

c = []
for i in range(len(l)):
    c.append(l.count(l[i]))
print(dict(zip(l, c)))
