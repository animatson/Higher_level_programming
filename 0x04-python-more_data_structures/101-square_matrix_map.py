#!/usr/bin/python3
def square_matrix_map(matrix = []):
    list(map(lambda list_: list(map((lambda x: x ** 2), list_)), matrix))