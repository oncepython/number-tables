def xijie(n):
    b = int((n ** 2 + n) / 2)
    c = int((1 + (8 * b + 1) ** 0.5) / 2)
    a = int(b + c)
    return a, b, c

ret = []
for i in range(10000):
    n = xijie(i)
    a = n[0]
    b = n[1]
    c = n[2]
    ret.append(f"a={a}, b={b}, c={c}\n")

with open("data.txt", "w") as f:
    f.write("".join(ret))
