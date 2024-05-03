import numpy as np
from scipy.linalg import qr, inv

def Matrix_Qudrat_extraction(A):
    rows, cols = A.shape

    # Split the array into four equal parts
    A_1_1 = A[:rows//2, :cols//2]
    A_1_2 = A[:rows//2, cols//2:]
    A_2_1 = A[rows//2:, :cols//2]
    A_2_2 = A[rows//2:, cols//2:]

    return A_1_1, A_1_2, A_2_1, A_2_2


def QR_tournament_pivoting(A, k):
    Q, R = qr(A)  # Thin QR factorization
    Qk = Q[:, :k]
    Rk = R[:k, :]
    return Qk, Rk

def LU_CRTP(A, k):
    m, n = A.shape
    
    # Step 3: Select k columns by using QR with tournament pivoting on A
    _, Pc = QR_tournament_pivoting(A, k)
    
    # Step 5: Select k rows by using QR with tournament pivoting on QTk
    QTk, _ = QR_tournament_pivoting(Pc.T, k)
    Pr = QTk.T

    # Step 6: Compute A¯ and PrQk
    A_1_1, A_1_2, A_2_1, A_2_2 = Matrix_Qudrat_extraction(A)
    PrQk = 0

    # Step 7: Compute L21 = A_2_1 * A_1_1_inverse
    
    L21 = A_2_1 * inv(A_1_1)
    
    # Extract Lk, Uk, and Rk
    Lk = 0
    Uk = 0
    Rk = 0
    
    return Pr, Pc, Lk, Uk, Rk

def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    k = 2  # Target rank
    Pr, Pc, Lk, Uk, Rk = LU_CRTP(A, k)
    print("Permutation matrix Pr:\n", Pr)
    print("\nPermutation matrix Pc:\n", Pc)
    print("\nMatrix Lk:\n", Lk)
    print("\nMatrix Uk:\n", Uk)
    print("\nMatrix Rk:\n", Rk)

main()