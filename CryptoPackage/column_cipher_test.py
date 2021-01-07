from CryptoPackage import column_cipher


def run_test():

    print("\n\nSimple Columnar Transposition cipher test")
    print("---------------------------------------------")

    col1 = 4
    col2 = 7
    key = "RAINBOW"
    string = "The quick brown fox jumps over the lazy dog."

    ciphertext = column_cipher.encrypt(col1, "", string)
    print(f"Ciphertext (4 columns, no key) : {ciphertext}")
    print(f"Plaintext (4 columns, no key) : {column_cipher.decrypt(col1, '', ciphertext)}")
    ciphertext = column_cipher.encrypt(col2, key, string)
    print(f"Ciphertext (7 columns, with key) : {ciphertext}")
    print(f"Plaintext (7 columns, with key) : {column_cipher.decrypt(col2, key, ciphertext)}")


if __name__ == "__main__":
    run_test()
