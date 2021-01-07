alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def verify_key(key, text):
    if len(key) != len(text):
        return False
    return True


def encrypt(key, plaintext):
    text_num_list = []
    key_num_list = []
    output = ""

    for char in plaintext:
        if char.upper() in alphabets:
            text_num_list.append(alphabets.index(char.upper()))
        else:
            text_num_list.append(-1)  # For non-alphabetic characters

    for char in key:
        if char.upper() in alphabets:
            key_num_list.append(alphabets.index(char.upper()))
        else:
            key_num_list.append(-1)  # For non-alphabetic characters

    for index, pair in enumerate(zip(text_num_list, key_num_list)):
        if -1 in pair:  # Non-alphabetic characters will be ignored (follow plaintext character)
            output += plaintext[index]
        else:
            output_num = sum(pair) % 26
            output += alphabets[output_num]

    return output.upper()


def decrypt(key, ciphertext):
    text_num_list = []
    key_num_list = []
    output = ""

    for char in ciphertext:
        if char.upper() in alphabets:
            text_num_list.append(alphabets.index(char.upper()))
        else:
            text_num_list.append(-1)  # For non-alphabetic characters

    for char in key:
        if char.upper() in alphabets:
            key_num_list.append(alphabets.index(char.upper()))
        else:
            key_num_list.append(-1)  # For non-alphabetic characters

    for index, pair in enumerate(zip(text_num_list, key_num_list)):
        if -1 in pair:  # Non-alphabetic characters will be ignored (follow plaintext character)
            output += ciphertext[index]
        else:
            if pair[0] < pair[1]:
                output_num = pair[0] + 26 - pair[1]
            # elif pair[0] == pair[1]:
            #     output_num = pair[0]
            else:
                output_num = pair[0] - pair[1]
            output += alphabets[output_num]

    return output.upper()
