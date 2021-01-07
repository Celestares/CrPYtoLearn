from CryptoPackage import vernam_cipher


def run_test():

    print("\n\nVernam cipher test")
    print("---------------------------------------------")

    key = "GOOD KEY 123"
    string = "Good day sir"

    ciphertext = vernam_cipher.encrypt(key, string)
    print(f"Ciphertext : {ciphertext}")
    print(f"Plaintext : {vernam_cipher.decrypt(key, ciphertext)}")


if __name__ == "__main__":
    run_test()
