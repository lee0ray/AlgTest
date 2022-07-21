def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


if __name__ == '__main__':
    print(gcd(1, 10))
    print(gcd(8, 16))
