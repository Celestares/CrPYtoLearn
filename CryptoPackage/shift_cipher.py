base64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='    # Q1, Q2, Q3
alphabets = "abcdefghijklmnopqrstuvwxyz"


def encrypt(key, plaintext_utf8, chars):
    ciphertext_utf8 = ""

    if chars == "alpha":
        for char in plaintext_utf8:

            if char.lower() in alphabets:
                pos = alphabets.index(char.lower())
                pos = (pos + key) % len(alphabets)
                if char.isupper():
                    ciphertext_utf8 += alphabets[pos].upper()
                else:
                    ciphertext_utf8 += alphabets[pos]
            else:
                ciphertext_utf8 += char
    else:
        for char in plaintext_utf8:

            if char in base64_chars:
                pos = base64_chars.index(char)
                pos = (pos + key) % len(base64_chars)
                ciphertext_utf8 += base64_chars[pos]
            else:
                ciphertext_utf8 += char

    return ciphertext_utf8


def decrypt(key, ciphertext_utf8, chars):
    decryptedtext_utf = ""

    if chars == "alpha":
        for char in ciphertext_utf8:

            if char.lower() in alphabets:
                pos = alphabets.index(char.lower())
                pos = (pos - key) % len(alphabets)
                if char.isupper():
                    decryptedtext_utf += alphabets[pos].upper()
                else:
                    decryptedtext_utf += alphabets[pos]
            else:
                decryptedtext_utf += char
    else:
        for char in ciphertext_utf8:

            if char in base64_chars:
                pos = base64_chars.index(char)
                pos = (pos - key) % len(base64_chars)
                decryptedtext_utf += base64_chars[pos]
            else:
                decryptedtext_utf += char

    return decryptedtext_utf
