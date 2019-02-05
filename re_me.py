#!/usr/bin/python3

c = lambda x, y : x + y
a = lambda x, y : x << y
f = lambda x, y : x % y
e = lambda x, y : x ^ y

g = 0x20
m = 0b01111111

flag_enc = [67, 108, 'A', 18176, 1968, 28416, 401408, 6684672, 0, 53, 47, 32, 51, 1680, 28416, 450560, 8192000]

def chonk(x):
    ret = []
    j = 4
    for i in x:
        ret.append(a(ord(i), j))
        j = j + 4
    return ret

def strange(key, s):
    hmmm = []
    for i in range(0, len(s)):
        hmmm.append(e(ord(key[i]), ord(s[i])))
    return hmmm

def encrypt(s):
    out = []
    out.append(f(c(ord(s[0]), 0xfb), m))
    out.append(e(ord(s[1]), g))
    out.append(s[2])
    out.append(a(ord(s[3]), 8))
    z = chonk(s[4:8])
    for i in z:
        out.append(i)
    out.append(ord(s[8]) ^ 0x75)
    p = strange(s[0:4], s[9:13])
    for i in p:
        out.append(i)
    z = chonk(s[13:18])
    for i in z:
        out.append(i)
    print(out)

def main():
    print("encrypt!")
    encrypt(flag_dec)


if __name__ == "__main__":
    main()

