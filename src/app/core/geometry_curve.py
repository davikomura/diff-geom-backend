from app.core.partials import compute_partials
from app.core.normals import compute_normals 
from app.core.first_fundamental_form import compute_first_fundamental_form
from app.core.second_fundamental_form import compute_second_fundamental_form
from app.core.curvatures import (
    compute_gaussian_curvature,
    compute_mean_curvature,
    compute_principal_curvatures,
    compute_normal_curvature
)

def compute_curve_data(x, y, z, u, v, curvature_type="gaussian", **kwargs):
    Xu, Xv = compute_partials(x, y, z, u, v)
    n = compute_normals(Xu, Xv)
    E, F, G = compute_first_fundamental_form(Xu, Xv)
    L, M, N = compute_second_fundamental_form(x, y, z, u, v, n)

    if curvature_type == "gaussian":
        K = compute_gaussian_curvature(E, F, G, L, M, N)
        return x, y, z, K

    elif curvature_type == "mean":
        H = compute_mean_curvature(E, F, G, L, M, N)
        return x, y, z, H

    elif curvature_type == "principal":
        H = compute_mean_curvature(E, F, G, L, M, N)
        K = compute_gaussian_curvature(E, F, G, L, M, N)
        k1, k2 = compute_principal_curvatures(H, K)
        return x, y, z, {"k1": k1, "k2": k2}

    elif curvature_type == "normal":
        a = kwargs.get("a", 1)
        b = kwargs.get("b", 1)
        kn = compute_normal_curvature(E, F, G, L, M, N, a, b)
        return x, y, z, kn

    else:
        raise ValueError(f"Unsupported curvature type: {curvature_type}")