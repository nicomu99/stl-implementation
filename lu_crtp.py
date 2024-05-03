from scipy.linalg import qr
import numpy as np

#input:
#A is a numpy matrix mxn
#P_c is a numpy permutation matrix nxn?
#k is an integer
#output:
#Q_k is a numpy matrix
#R_k is a numpy matrix
def lu_crtp_4(A, P_c, k):
    AP_c = np.dot(A, P_c)
    print("AP_c:")
    print(AP_c)
    AP_c_selected_columns = AP_c[:, :k]
    print("AP_c_selected_columns:")
    print(AP_c_selected_columns)
    Q_k, R_k = np.linalg.qr(AP_c_selected_columns)
    return Q_k, R_k

def lu_crtp(a, k):
    # According to https://epubs-siam-org.uaccess.univie.ac.at/doi/epdf/10.1137/13092157X QR_TP is the same
    # as RRQR. For a faster implementation, we therefore decided on using scipy's LAPACK interface.
    # Select k columns by using QR with tournament pivoting on A
    _, _, p_c = qr(a, pivoting=True)
    p_c = p_c[:, k]

    # Compute the thin QR factorization of the selected columns
    q_k, _ = lu_crtp_4(a, p_c, k)

    # Select k rows by using QR with tournament pivoting on Q^T_k
    p_r = qr(q_k.T, pivoting=True)
    p_r = p_r[:, k]

    # Let A_ = P ...
    a_dash = p_r * a * p_c
    rows, cols = a_dash.shape

    # Compute L_k
    a_upper_left = a_dash[:rows//2, :cols//2]
    a_lower_left = a_dash[rows//2:, :cols//2]
    inv_a_upper_left = np.linalg.inv(a)
    l_21 = a_lower_left * inv_a_upper_left
    i = np.identity(a_dash//2, k)
    l_k = np.vstack(i, l_21)
    return l_k
