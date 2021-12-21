import scipy.optimize as opt
import numpy as np

from model import Model

def get_eta(m: Model, Y: float, H: float, K: float, beta = 1.) -> float:
    """
    Numerically computes `eta` assuming a value for beta based on a `model` instance and a value of `Y`, `K` and, `H`. 

    The computation is done numerically and not analytically to abstract from the output function.
    """

    def equilibrium(p):
        eta = p[0]
        deltaY = Y - m.Y(H, K, eta)
        deltaK = K - m.Ks(H, K, eta)

        deltaH = H - m.Hs(H, K, eta, beta)

        return np.square(deltaY + deltaH + deltaK)

    result = opt.minimize(
        equilibrium, 
        [0.5], # Initial values
        bounds=((0., 1.), ) # Solution constraints
    )

    sol = result.x
    error = result.fun

    return sol, error

def get_parameters(m: Model, Y: float, H: float, K: float) -> float:
    """
    Numerically computes `eta` and `beta` based on a `model` instance and a value of `Y`, `K` and, `H`. 

    The computation is done numerically and not analytically to abstract from the output function.
    """

    def equilibrium(p):
        eta, beta = p
        deltaY = Y - m.Y(H, K, eta)
        deltaK = K - m.Ks(H, K, eta)

        deltaH = H - m.Hs(H, K, eta, beta)

        return np.square(deltaY + deltaH + deltaK)

    result = opt.minimize(
        equilibrium, 
        [0.5, 1.], # Initial values
        bounds=((0., 1.), (0.1, None)) # Solution constraints
    )

    sol = result.x
    error = result.fun

    return sol, error
