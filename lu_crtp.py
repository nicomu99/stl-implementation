import numpy as np

def lu_crtp(matrix, rank):
    for row in matrix:
        print(row)

def main():
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    rank = 1
    
    lu_crtp(matrix, rank)

main()