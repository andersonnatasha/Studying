def make_pascal_triangle(n):
    # """write a function to print out pascal's triangle to n depth, given n
    # >>> make_pascal_triangle(1)
    # 1
    # >>> make_pascal_triangle(4)
    # 1 3 3 1
    # """"
    # # ans = []

    if n == 1:
        return 1

    array = [1]

    for i in range(n-1):
        array = [0] + array + [0]
        array = [sum(array[i:i+2]) for i in range(len(array)-1)]
    return array


def sort_diagonally(matrix):
    """
    >>> sort_diagonally([1, 4, -2], [-2, 3, 4], [1, -2, -2])
    [3, 3, 4], [3, 4, 1], [1, -2, -2])
    """

    arr = [-2, -2, 1, 1, 4, 4, 3, 3, 3]

    def get_diagonal_pos(diag_row, diag_column,):
        # check can you go left, if you can then go subtract one from the col
        if diag_column - 1 >= 0:
            return (diag_row, diag_column - 1)
        # if you cant then add one to the row
        if diag_row - 1 >= 0:
            return (diag_row - 1, diag_column)

        return (None, None)

    def put_in_matrix(arr, current_row, current_column, diag_row, diag_column, matrix):

        max_row = len(matrix)
        max_column = len(matrix[0])

        if 0 <= current_row < max_row and 0 <= current_column < max_column:

            matrix[current_row][current_column] = arr[0]
            return put_in_matrix(arr[1:], current_row - 1, current_column + 1, diag_row, diag_column, matrix)

        diag_row, diag_column = get_diagonal_pos(diag_row, diag_column)

        if diag_column != None and diag_row != None:
            put_in_matrix(arr, diag_row, diag_column,
                          diag_row, diag_column,  matrix)

    put_in_matrix(arr, len(matrix) - 1, len(
        matrix[0]) - 1, len(matrix) - 1, len(matrix[0]) - 1, matrix)

    return matrix


# sort_diagonally([[1, 4, -2], [-2, 3, 4], [3, 1, 3]])


def maximalPalindrome(s):
    """
    give s, find the max palindrome. If there re multiple longest palindromes, return the one that is lexicographically smallest
    >>> maximalPalindrome("aaabb")
    ababa
    """

    occurances = {}

    for letter in s:
        occurances[letter] = occurances.get(letter, 0) + 1

    begining = []
    middle = []
    end = []

    odds = []   # (a, 3) (b, 3)
    evens = []  # (#c, 2)

    for key, value in occurances.items():
        if value % 2 != 0:
            odds.append((key, value))
        else:
            evens.append((key, value))

    odds = sorted(odds, key=lambda i: i[0])
    odds = sorted(odds, key=lambda i: i[1], reverse=True)

    # go through odds, put th efirst element add one to middle and add the remaining to even and subtract one from other and add to even

    middle = [odds[0][0]]
    for element in odds:
        if element[1] > 1:
            evens.append((element[0], element[1] - 1))

    evens = sorted(evens, key=lambda i: i[0])
    # print(evens)

    for element in evens:
        for i in range(element[1]//2):
            begining.append(element[0])
            end.insert(0, element[0])

    return "".join(begining + middle + end)


maximalPalindrome("aaabbbcc")


def secondary_diagonal(matrix):
    """Given a square matrix of positive integers, sort thr number in each of its diagonals parallel to the secondary diagonal.
    Each diagonal should contain the same set of numbers as before but sorted in ascending order from the bottom-left to top-right"""
    def get_next_diag_point(coordinates, max_row, max_column):
        # if i can go down do that
        if coordinates[0] < max_row:
            return (coordinates[0] + 1, coordinates[1])
        # elif if can go right do that
        if coordinates[1] < max_column:
            return(coordinates[0], coordinates[1] + 1)
        # else return none
        else:
            return (None, None)

    def sort_diag(matrix, diag_coordinates, max_row, max_column):

        current_row = diag_coordinates[0]
        current_column = diag_coordinates[1]

        diag_values = []

        while 0 <= current_row <= max_row and 0 <= current_column <= max_row:
            diag_values.append(matrix[current_row][current_column])
            current_row -= 1
            current_column += 1

        current_row = diag_coordinates[0]
        current_column = diag_coordinates[1]

        while 0 <= current_row <= max_row and 0 <= current_column <= max_row:
            diag_values = sorted(diag_values)
            matrix[current_row][current_column] = diag_values.pop(0)
            current_row -= 1
            current_column += 1

        diag_coordinates = get_next_diag_point(
            diag_coordinates, max_row, max_column)

        if diag_coordinates[0] != None:
            return sort_diag(matrix, diag_coordinates, max_row, max_column)

    sort_diag(matrix, (0, 0), len(matrix) - 1, len(matrix[0]) - 1)

    return matrix


print(secondary_diagonal(
    [[1, 3, 9, 4], [9, 5, 7, 7], [3, 6, 9, 7], [1, 2, 2, 2]]))
