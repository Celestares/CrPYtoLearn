def verify_col(col):
    if col < 2:
        return False
    return True


def verify_inputs(col, key):
    if key == "":
        if col < 2:
            return False
    else:
        if col < 2:
            return False
        elif len(key) != col:
            return False

    if not key.isalpha():
        return False

    return True


def encrypt(col, key, plaintext):
    matrix = []
    sublist = []
    suboutput = ""
    output = []

    for char in plaintext:
        sublist.append(char)
        if len(sublist) == col:
            matrix.append(sublist)
            sublist = []
    if sublist:  # Check if there is remainings
        sublist = sublist + [" "] * (col - len(sublist))
        matrix.append(sublist)

    for c in range(col):
        for r in range(len(matrix)):
            suboutput += matrix[r][c]
        output.append(suboutput)
        suboutput = ""

    if not key:
        return "".join(output)
    else:
        temp_output = output
        output = []
        unsorted_key = [char for char in key.upper()]
        sorted_key = sorted(unsorted_key)
        for letter in sorted_key:
            column = unsorted_key.index(letter)
            output.append(temp_output[column])
            unsorted_key[column] = "_"
        return "".join(output)


def decrypt(col, key, ciphertext):
    matrix = []
    row = len(ciphertext) // col
    start = 0
    output = []

    for r in range(col):
        matrix.append([char for char in ciphertext[start:start + row]])
        start += row

    if key:  # Sorting the rows in order based on key
        temp_matrix = matrix
        matrix = []
        unsorted_key = [char for char in key.upper()]
        sorted_key = sorted(unsorted_key)
        for letter in unsorted_key:
            row_index = sorted_key.index(letter)
            matrix.append(temp_matrix[row_index])
            sorted_key[row_index] = "_"

    for r in range(row):
        suboutput = ""
        for c in range(col):
            suboutput += matrix[c][r]
        output.append(suboutput)
    return "".join(output).rstrip()


# T h e   q u i
# c k   b r o w
# n   f o x   j
# u m p s   o v
# e r   t h e
# l a z y   d o
# g .
