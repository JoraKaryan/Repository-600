#ex-7

bar = "What! is! this book about !this book! is about python coding"

def foo(bar:str):
    for i in range(len(bar)):
        if 0 <= ord(bar[i]) <= 31 or 33<= ord(bar[i])<=64 or 91 <= ord(bar[i]) <= 96 or 123 <= ord(bar[i]) <= 127:
            bar= bar.replace(bar[i], "")
            return bar

bar = (foo(bar))

l = bar.split(" ")

c = []
for i in range(len(l)):
    c.append(l.count(l[i]))
print(dict(zip(l, c)))


