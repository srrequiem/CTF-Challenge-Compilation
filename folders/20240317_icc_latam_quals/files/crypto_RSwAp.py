from random import randint
from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from secret import flag

def swap(n, p1, p2):
    s = [x for x in str(n)]
    s[p1], s[p2] = s[p2], s[p1]
    return int(''.join(s))

p = getPrime(1024)
q = 1

while not isPrime(q) or p == q:
    l = len(str(p))
    a, b = randint(1,l-2), randint(1,l-2)
    q = swap(p, a, b)

n = p*q
e = 65537
m = bytes_to_long(flag)

print(f"n = {n}")
print(f"enc = {pow(m,e,n)}")
