from CryptoPackage import dhkey_exchange


def run_test():

    print("\n\nDiffie-Hellman Key Exchange test")
    print("---------------------------------------------")

    n = 5
    g = 19
    not_prime = 20
    x = 515
    y = 286
    if dhkey_exchange.is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
    if dhkey_exchange.is_prime(not_prime):
        print(f"{not_prime} is a prime number")
    else:
        print(f"{not_prime} is not a prime number")

    if dhkey_exchange.is_prime(n) and dhkey_exchange.is_prime(g):
        key = dhkey_exchange.generate_key(n, g, x, y)
        print(f"Symmetric key is {key} using n = {n}, g = {g}, x = {x}, y = {y}")


if __name__ == "__main__":
    run_test()
