import numpy as np

def compute_first_fundamental_form(Xu, Xv):
 
    E = np.einsum('...i,...i', Xu, Xu)
    F = np.einsum('...i,...i', Xu, Xv)
    G = np.einsum('...i,...i', Xv, Xv)

    return E, F, G
