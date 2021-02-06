
# Consider a square matrix with sides of even length.

# Define its 0-border as the union of left and right columns as well as top and bottom rows.
# Now consider the initial matrix without the 0-border. Its 0-border is 1-border for the initial matrix. In the same way one can define 2-border, 3-border, etc.

# Given a square matrix, find sums of elements for each of the matrix borders.

# Example:

# For matrix = [[1,  2,  2,  3],
#               [0,  1,  0,  2],
#               [4, -1, -1, -3],
#               [4, -1, -1,  3]


# the output should be borderSums(matrix) = [16, -1].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.array.integer matrix

# Array of arrays of integers representing a square matrix with sides of even length.

# Guaranteed constraints:
# 4 ≤ matrix.length ≤ 10,
# matrix[i].length = matrix.length,
# -10 ≤ matrix[i][j] ≤ 10.

# [output] array.integer

# An array A such that A[i] is equal to the sum of elements of the i-border of matrix.
# The length of the A should be half of the length of the matrix side.

# matrix = [[1,  2,  2,  3],
#           [0,  1,  0,  2],
#           [4, -1, -1, -3],
#           [4, -1, -1,  3]]


matrix = [[1,  2,  2,  3],
          [0,  1,  0,  2],
          [4, -1, 2, -3],
          [4, -1, -1,  3],
          [3,  10,  4,  6],
          [6,  4,  17,  9],
          [6,  4,  17,  9],
          [6,  4,  17,  9],
          ]

print(sum([1, 2, 2, 3, 6, 4, 17, 9, 0, 4, 4, 3, 6, 6, 2, -3, 3, 6, 9, 9]))
print(sum([1, 0, -1, 2, -1, -1, 10, 4, 4, 17, 4, 17]))

def borderSumRecursively(matrix, answer):

    if not matrix[0]:
        return answer

    # initalize sum
    sum_ = 0

    # get top
    top = matrix[0]
    # get bottom
    bottom = matrix[-1]
    # get left
    left = list(map(lambda list_: list_[0], matrix[1:-1]))
    # get right
    right = list(map(lambda list_: list_[-1], matrix[1:-1]))
    # get sum
    sum_ = sum(top + bottom + left + right)
    # add sum to answer
    answer.append(sum_)
    # pop top from matrix
    matrix.pop(0)
    # pop bottom from matrix
    matrix.pop(-1)
    # remove 0 from each matrix
    list(map(lambda list_: list_.pop(0), matrix))
    # remove -1 from each matrix
    list(map(lambda list_: list_.pop(-1), matrix))


    return borderSumRecursively(matrix, answer)


print(borderSumRecursively(matrix, []))


def borderSum(matrix):
    answer = []

    for i in range(len(matrix[0])//2):
        # initalize sum
        sum_ = 0

        # get top
        top = matrix[0]
        # get bottom
        bottom = matrix[-1]
        # get left
        left = list(map(lambda list_: list_[0], matrix[1:-1]))
        # get right
        right = list(map(lambda list_: list_[-1], matrix[1:-1]))
        # get sum
        sum_ = sum(top + bottom + left + right)
        # add sum to answer
        answer.append(sum_)
        # pop top from matrix
        matrix.pop(0)
        # pop bottom from matrix
        matrix.pop(-1)
        # remove 0 from each matrix
        list(map(lambda list_: list_.pop(0), matrix))
        # remove -1 from each matrix
        list(map(lambda list_: list_.pop(-1), matrix))

    return answer

print(borderSum(matrix))