from .sphere import parametrize_sphere
from .torus import parametrize_torus
from .enneper import parametrize_enneper
from .helicoid import parametrize_helicoid
from .hyperbolic_paraboloid import parametrize_hyperbolic_paraboloid
from .elliptic_paraboloid import parametrize_elliptic_paraboloid

curve_parametrizations = {
    "sphere": parametrize_sphere,
    "torus": parametrize_torus,
    "enneper": parametrize_enneper,
    "helicoid": parametrize_helicoid,
    "hyperbolic_paraboloid": parametrize_hyperbolic_paraboloid,
    "elliptic_paraboloid": parametrize_elliptic_paraboloid,
}
