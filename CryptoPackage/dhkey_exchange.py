def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_key(n, g, x, y):
    a = (g ** x) % n
    b = (g ** y) % n

    k1 = (b ** x) % n
    k2 = (a ** y) % n

    if k1 == k2:
        return k1

