import numpy


def index_to_node(i, j, n):
    return (i - 1) * n + j


def node_to_index(index, n):
    i, j = divmod(index, n)
    if i == 0:
        i = 1
    else:
        i += 1
    if j == 0:
        j = n
        i -= 1
    return i, j


def move_in_matrix(self, n, dimension_index, direction):
            matrix_length = numpy.sqrt(n)
            matrix_location = node_to_index(self.location, n)
            previous_location = matrix_location
            matrix_location[dimension_index] += direction
            if matrix_location[dimension_index] < 0 or matrix_location[dimension_index] > matrix_length:
                matrix_location = previous_location
            self.location = index_to_node(matrix_location[0], matrix_location[1], n)
