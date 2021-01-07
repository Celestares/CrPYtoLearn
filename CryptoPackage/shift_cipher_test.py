from CryptoPackage import shift_cipher


def run_test():

    print("\n\nShift cipher test")
    print("---------------------------------------------")

    key = 3

    plaintext = "HELLO"     # Q1, Q2
    ciphertext = shift_cipher.encrypt(key, plaintext, "alpha")
    decryptedtext = shift_cipher.decrypt(key, ciphertext, "alpha")
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    plaintext = "Hello!"    # Q1, Q2
    ciphertext = shift_cipher.encrypt(key, plaintext, "alpha")
    decryptedtext = shift_cipher.decrypt(key, ciphertext, "alpha")
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    plaintext = "Hello123+/="   # Q3
    ciphertext = shift_cipher.encrypt(key, plaintext, "b64")
    decryptedtext = shift_cipher.decrypt(key, ciphertext, "b64")
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")


if __name__ == "__main__":
    run_test()
