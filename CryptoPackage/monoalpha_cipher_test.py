from CryptoPackage import monoalpha_cipher


def run_test():

    print("\n\nRunning Mono-alphabetic cipher test")
    print("---------------------------------------------")

    string = "The quick brown fox jumps over the lazy dog."
    fixed_key = "zyxwvutsrqponmlkjihgfedcba"
    random_key = monoalpha_cipher.generate_key()

    if monoalpha_cipher.validate_key(fixed_key):
        print(f"{fixed_key} is valid.")
    if monoalpha_cipher.validate_key(random_key):
        print(f"{random_key} is valid.")

    print(f"Input text : {string}")
    print("----------------------------------------------------------------------")
    ciphertext = monoalpha_cipher.encrypt(fixed_key, string)
    print(f"Ciphertext (Fixed key) : {ciphertext}")
    print(f"Plaintext (Fixed key) : {monoalpha_cipher.decrypt(fixed_key, ciphertext)}")
    ciphertext = monoalpha_cipher.encrypt(random_key, string)
    print(f"Ciphertext (Random key) : {ciphertext}")
    print(f"Plaintext (Random key) : {monoalpha_cipher.decrypt(random_key, ciphertext)}")


if __name__ == "__main__":
    run_test()
