def validate_row(row):
    if row < 2:
        return False
    return True


def encrypt(row, plaintext):
    matrix = []
    for i in range(row):
        matrix.append([])

    reverse = False
    row_index = 0
    row_boundary = (0, row - 1)
    output = ""

    for char in plaintext:
        matrix[row_index].append(char)
        if reverse:
            row_index -= 1
        else:
            row_index += 1
        if row_index in row_boundary:
            reverse = not reverse  # Swap between True and False state

    for line in matrix:
        output += "".join(line)

    return output


def decrypt(row, ciphertext):
    output = ""

    # Determine and calculate number of characters for each row (segments)
    length = len(ciphertext)
    segment_num = 2 * (row - 1)
    base_segment_len = length // segment_num
    remains = length - (base_segment_len * segment_num)

    segment_list = [base_segment_len, base_segment_len]
    for i in range(row - 2):
        segment_list.insert(1, base_segment_len * 2)

    row_index = 0
    reverse = False
    row_boundary = (0, row - 1)
    for i in range(remains):
        segment_list[row_index] += 1
        # Counter that counts up and down based on boundary
        if reverse:
            row_index -= 1
        else:
            row_index += 1
        if row_index in row_boundary:
            reverse = not reverse  # Swap between True and False state

    # Formatting matrix based on segment list
    start = 0
    matrix = []
    for segment in segment_list:
        matrix.append(ciphertext[start:start + segment])
        start += segment
    for index, string in enumerate(matrix):
        matrix[index] = [char for char in string]

    # Reading matrix
    row_index = 0
    reverse = False
    while len(output) != length:
        output += matrix[row_index].pop(0)
        if reverse:
            row_index -= 1
        else:
            row_index += 1
        if row_index in row_boundary:
            reverse = not reverse  # Swap between True and False state

    return output
