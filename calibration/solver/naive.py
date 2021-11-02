import scipy.optimize as opt

from model import Model


def get_eta(model: Model, Y: float, H: float, K: float) -> float:
    """
    Numerically computes `eta` based on a `model` instance and a value of `Y`, `K` and, `H`. 

    The computation is done numerically and not analytically to abstract from the output function.
    """

    def equilibrium(eta):

        deltaY = Y - model.Y(H, K, eta)
        deltaK = K - model.Ks(H, K, eta)
        deltaH = H - model.Hs(H, K, eta)

        return deltaY + deltaH + deltaK

    return opt.newton(equilibrium, )
