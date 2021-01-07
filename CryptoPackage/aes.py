from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def get_random_key(bit_size):  # 128, 192, 256
    key = get_random_bytes(int(bit_size / 8))
    return key


def convert_to_bin(string):  # Convert string to binary literally and exactly 'hello' -> b'hello'
    # Because it uses eval(), let say the string is "\xqw\m2f\'eqw"
    # and if run the code eval("b'%s'" % string), you can say that sort of an injection attack have happened where
    # the code would become eval("b'\xqw\m2f\'eqw'"), and as you can see when we eval this it would give us an error
    # because it evaluated the byte string b'\xqw\m2f\' and the remaining eqw' creates a syntax error
    # you can interpret it as bytes = b'\xqw\m2f\'eqw'
    # which if u try to assign that to the variable "bytes" it would create a syntax error
    # try testing it out by running the this python file
    try:
        return eval("b\"%s\"" % string)
    except:
        return eval("b\'%s\'" % string)


def convert_to_str(binary):  # Convert binary to string literally and exactly b'hello' -> 'hello'
    return f"{binary}"[2: -1]


def encrypt_ecb(key, plaintext):
    cipher_key = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher_key.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def decrypt_ecb(key, ciphertext):
    cipher_key = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher_key.decrypt(ciphertext), AES.block_size)
    return plaintext


def encrypt_cbc(key, plaintext):
    cipher_key = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher_key.encrypt(pad(plaintext, AES.block_size))
    return cipher_key.iv, ciphertext


def decrypt_cbc(key, iv, ciphertext):
    cipher_key = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher_key.decrypt(ciphertext), AES.block_size)
    return plaintext


def encrypt_cfb(key, plaintext):
    cipher_key = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher_key.encrypt(pad(plaintext, AES.block_size))
    return cipher_key.iv, ciphertext


def decrypt_cfb(key, iv, ciphertext):
    cipher_key = AES.new(key, AES.MODE_CFB, iv)
    plaintext = unpad(cipher_key.decrypt(ciphertext), AES.block_size)
    return plaintext


def encrypt_ofb(key, plaintext):
    cipher_key = AES.new(key, AES.MODE_OFB)
    ciphertext = cipher_key.encrypt(pad(plaintext, AES.block_size))
    return cipher_key.iv, ciphertext


def decrypt_ofb(key, iv, ciphertext):
    cipher_key = AES.new(key, AES.MODE_OFB, iv)
    plaintext = unpad(cipher_key.decrypt(ciphertext), AES.block_size)
    return plaintext


if __name__ == "__main__":  # Running this .py file will create an error, is to demostrate convert to binary error
    test_string = r"\xqw\m2f\'eqw"  # r"" means raw string
    byte = eval("b'%s'" % test_string)
    # byte = b'\xqw\m2f\'eqw'
    # line 81 creates same error as line 80
