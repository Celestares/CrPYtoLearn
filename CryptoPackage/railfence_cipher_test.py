from CryptoPackage import railfence_cipher


def run_test():

    print("\n\nRail Fence cipher test")
    print("---------------------------------------------")

    row1 = 3
    row2 = 7
    string = "The quick brown fox jumps over the lazy dog."

    ciphertext = railfence_cipher.encrypt(row1, string)
    print(f"Ciphertext (3 rows) : {ciphertext}")
    print(f"Plaintext (3 rows) : {railfence_cipher.decrypt(row1, ciphertext)}")
    ciphertext = railfence_cipher.encrypt(row2, string)
    print(f"Ciphertext (7 rows) : {ciphertext}")
    print(f"Plaintext (7 rows) : {railfence_cipher.decrypt(row2, ciphertext)}")


if __name__ == "__main__":
    run_test()
