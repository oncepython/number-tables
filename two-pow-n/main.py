buf = ""
f = open("two-pow-n.txt", "a")
for n in range(10000):
    buf += f"2^{n} = {2**n}\n"
    if n%100==0:print(n)
f.write(buf)
f.close()
