def xijie(n):
    b = int((n ** 2 + n) / 2)
    c = int((1 + (8 * b + 1) ** 0.5) / 2)
    a = int(b + c)
    return a, b, c

for i in range(100):
    print(xijie(i))
