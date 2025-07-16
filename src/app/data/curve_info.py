# src/app/data/curve_info.py
curve_info = {
    "sphere": {
        "name": "sphere",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = (\sin u \cos v,\ \sin u \sin v,\ \cos u)",
        "domain": r"u \in [0, \pi],\ v \in [0, 2\pi]"
    },
    "torus": {
        "name": "torus",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = ((R + r \cos v) \cos u,\ (R + r \cos v) \sin u,\ r \sin v)",
        "domain": r"u, v \in [0, 2\pi]"
    },
    "enneper": {
        "name": "enneper",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = \left(u - \frac{u^3}{3} + uv^2,\ -v + \frac{v^3}{3} - vu^2,\ u^2 - v^2\right)",
        "domain": r"u, v \in [-2, 2]"
    },
    "helicoid": {
        "name": "helicoid",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = (a v \cos u,\ a v \sin u,\ b u)",
        "domain": r"u \in [-2\pi, 2\pi],\ v \in [-1, 1]"
    },
    "hyperbolic_paraboloid": {
        "name": "hyperbolic_paraboloid",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = \left(u,\ v,\ \frac{u^2}{a^2} - \frac{v^2}{b^2} \right)",
        "domain": r"u, v \in [-1, 1]"
    },
    "elliptic_paraboloid": {
        "name": "elliptic_paraboloid",
        "type": "surface",
        "latex": r"\vec{X}(u, v) = \left(u,\ v,\ \frac{u^2}{a^2} + \frac{v^2}{b^2} \right)",
        "domain": r"u, v \in [-1, 1]"
    }
}
