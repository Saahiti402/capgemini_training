import unittest
def test_flip_and_reverse_from_input(a, input_matrix):
    result = []

    for i in range(a):
        var = input_matrix[i]
        result.append(var)

    for o in range(a):
        result[o] = result[o][::-1]

    for j in range(a):
        for g in range(len(result[j])):
            if result[j][g] == 0:
                result[j][g] = 1
            else:
                result[j][g] = 0

    return result
