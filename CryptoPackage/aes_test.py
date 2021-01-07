from CryptoPackage import aes


def run_test():

    print("\n\nAES test")
    print("---------------------------------------------")

    key_value = aes.get_random_key(192)
    string = "Testing".encode("utf-8")

    etext = aes.encrypt_ecb(key_value, string)
    print(f"Ciphertext (ECB) : {etext}")
    print(f"Plaintext (ECB) : {aes.decrypt_ecb(key_value, etext)}")
    iv_value, etext = aes.encrypt_cbc(key_value, string)
    print(f"Ciphertext (CBC) : {etext}")
    print(f"Plaintext (CBC) : {aes.decrypt_cbc(key_value, iv_value, etext)}")
    iv_value, etext = aes.encrypt_cfb(key_value, string)
    print(f"Ciphertext (CFB) : {etext}")
    print(f"Plaintext (CFB) : {aes.decrypt_cfb(key_value, iv_value, etext)}")
    iv_value, etext = aes.encrypt_ofb(key_value, string)
    print(f"Ciphertext (OFB) : {etext}")
    print(f"Plaintext (OFB) : {aes.decrypt_ofb(key_value, iv_value, etext)}")


if __name__ == "__main__":
    run_test()
