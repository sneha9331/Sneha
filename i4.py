def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo //= 2
    return res

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    d = modInverse(e, phi)
    if d == -1:
        raise ValueError("Modular inverse not found")
    return e, d, n

def encrypt(m, e, n):
    return power(m, e, n)

def decrypt(c, d, n):
    return power(c, d, n)

# MAIN
p = int(input("Enter the prime number(p): "))
if not is_prime(p):
    print("p is not a prime number")
    exit()

q = int(input("Enter the prime number(q): "))
if not is_prime(q):
    print("q is not a prime number")
    exit()

e, d, n = generate(p, q)
print("Public Key: ", (e, n))
print("Private Key:", (d, n))

M = int(input("Enter the message (as a number): "))
c = encrypt(M, e, n)
print("Encryption:", c)
print("Decryption:", decrypt(c, d, n))