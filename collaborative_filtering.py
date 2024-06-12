import numpy as np
from sklearn.decomposition import NMF, PCA
from sklearn.preprocessing import StandardScaler
from lu_crtp import lu_crtp

def nmf_wrapper(data, n_components=3):
    
    # Perform NMF
    nmf = NMF(n_components=n_components).fit(data)
    H = nmf.components_
    W = nmf.transform(data)

    # Reconstruct initial array with new recommendations
    return np.dot(W, H)


def nmf_pca_wrapper(data, n_components=3):
    std_scaler = StandardScaler()
    data_scaled = std_scaler.fit_transform(data)

    pca = PCA(n_components=n_components) 
    data_reduced = pca.fit_transform(data_scaled)

    # NMF needs the data to be larger than 0, so we scale the data up
    min_value = np.min(data_reduced)
    data_shifted = data_reduced - min_value

    nmf = NMF(n_components=n_components).fit(data_shifted)
    H = nmf.components_
    W = nmf.transform(data_shifted)

    # Predict ratings & reformat
    pred = np.dot(W, H)
    pred += min_value
    return pca.inverse_transform(pred)


def lu_crtp_wrapper(data, n_components=3):
    U, S, V = np.linalg.svd(data, full_matrices=False)
    U = U[:, :n_components]
    S = np.diag(S[:n_components])
    V = V[:n_components, :]

    V_new = np.dot(U, np.dot(S, V))

    _, _, l_k, u_k, _ = lu_crtp(V_new, n_components)

    return np.dot(l_k, u_k)