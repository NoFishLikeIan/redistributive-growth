import scipy.optimize as opt
import numpy as np

from model import Model


def get_eta(m: Model, Y: float, H: float, K: float) -> float:
    """
    Numerically computes `eta` based on a `model` instance and a value of `Y`, `K` and, `H`. 

    The computation is done numerically and not analytically to abstract from the output function.
    """

    def equilibrium(eta):
        deltaY = Y - m.Y(H, K, eta)
        deltaK = K - m.Ks(H, K, eta)
        deltaH = H - m.Hs(H, K, eta)

        return np.square(deltaY + deltaH + deltaK)

    result = opt.minimize(equilibrium, 0.5, bounds=((0., 1.), ))

    sol = result.x[0]
    error = result.fun

    return sol, error
