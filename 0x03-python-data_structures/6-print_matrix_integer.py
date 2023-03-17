#!/usr/bin/python3
def pringt_matrix_integet(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))
