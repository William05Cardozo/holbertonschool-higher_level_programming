#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in matrix:
        nmatrix.append(list(map(lambda x: x ** 2, i)))
    return(nmatrix)
