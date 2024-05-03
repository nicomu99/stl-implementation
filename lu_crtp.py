#input:
#A is a numpy matrix mxn
#P_c is a numpy permutation matrix nxn?
#k is an integer
#output:
#Q_k is a numpy matrix
#R_k is a numpy matrix
def lu_crtp_4(A, P_c, k):
    AP_c = np.dot(A, P_c)
    AP_c_selected_columns = AP_c[:, :k]
    Q_k, R_k = np.linalg.qr(AP_c_selected_columns)
    return Q_k, R_k

def lu_crtp():
    pass