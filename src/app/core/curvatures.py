import numpy as np

def compute_gaussian_curvature(E, F, G, L, M, N):

    denominator = E * G - F**2
    numerator = L * N - M**2
    K = numerator / denominator
    return K

def compute_mean_curvature(E, F, G, L, M, N):

    denominator = E * G - F**2
    numerator = E * N + G * L - 2 * F * M
    H = numerator / (2 * denominator)
    return H

def compute_principal_curvatures(H, K):

    discriminant = np.sqrt(np.clip(H**2 - K, 0, None))
    k1 = H + discriminant
    k2 = H - discriminant
    return k1, k2

def compute_normal_curvature(E, F, G, L, M, N, a=1, b=1):

    numerator = L * a**2 + 2 * M * a * b + N * b**2
    denominator = E * a**2 + 2 * F * a * b + G * b**2
    kn = numerator / denominator
    return kn
