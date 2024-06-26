from scipy.linalg import qr
import numpy as np

# input:
# A is a numpy matrix mxn
# P_c is a permutation matrix as an int ndarray of shape (N,)
# k is an integer
# output:
# Q_k is a numpy matrix
# R_k is a numpy matrix
def lu_crtp_4(A, P_c, k):
    AP_c = A[:, P_c]
    AP_c_selected_columns = AP_c[:,:k]
    Q_k, R_k = np.linalg.qr(AP_c_selected_columns)
    return Q_k, R_k

# input:
# a is a numpy matrix mxn
# k is an even integer
def lu_crtp(a, k):
    # According to https://epubs-siam-org.uaccess.univie.ac.at/doi/epdf/10.1137/13092157X QR_TP is the same
    # as RRQR. For a faster implementation, we therefore decided on using scipy's LAPACK interface.
    # Select k columns by using QR with tournament pivoting on A
    _, _, p_c = qr(a, pivoting=True)

    # Compute the thin QR factorization of the selected columns
    q_k, r_k = lu_crtp_4(a, p_c, k)

    # Select k rows by using QR with tournament pivoting on Q^T_k
    _, _, p_r = qr(q_k.T, pivoting=True)

    # Let A_ = P ...
    a_dash = a[:,p_c]
    a_dash = a_dash[p_r,:]
    rows, cols = a_dash.shape
    
    # Separate into block matrices
    a_dash_11 = a_dash[:k, :k]
    a_dash_21 = a_dash[k:, :k]
    a_dash_12 = a_dash[:k, k:]

    # Compute L_21
    inv_a_dash_11 = np.linalg.inv(a_dash_11)
    l_21 = np.dot(a_dash_21, inv_a_dash_11)
    
    # Stack the block matrices
    i = np.identity(k)
    l_k = np.vstack((i, l_21))
    u_k = np.hstack((a_dash_11, a_dash_12))
    return p_r, p_c, l_k, u_k, r_k

# returns true if A and the approximation is equal
def compareApprox(A, p_r, p_c, l_k, u_k):
    approx = np.dot(l_k, u_k)
    print("approx:")
    print(approx)
    PA = p_A = A[p_r, :]
    PA = p_A[:, p_c]
    print("PA:")
    print(PA)
    return np.allclose(approx, PA)

