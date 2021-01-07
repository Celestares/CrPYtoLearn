from random import shuffle


def generate_key():
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = [s for s in alphabets]
    shuffle(alpha_list)
    return "".join(alpha_list)


def validate_key(key):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = [s for s in alphabets]
    for alpha in key:
        if alpha.upper() in alpha_list:
            alpha_list.remove(alpha.upper())
        else:
            return False
    if alpha_list:  # Make sure that list is empty
        return False
    return True


def encrypt(key, plaintext):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    for char in plaintext:
        if char.upper() in alphabets:
            cipher_index = alphabets.index(char.upper())
            if char.isupper():
                output += key[cipher_index].upper()
            else:
                output += key[cipher_index].lower()
        else:
            output += char

    return output


def decrypt(key, ciphertext):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    for char in ciphertext:
        if char.upper() in alphabets:
            plain_index = key.upper().index(char.upper())
            if char.isupper():
                output += alphabets[plain_index].upper()
            else:
                output += alphabets[plain_index].lower()
        else:
            output += char

    return output
