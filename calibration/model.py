import math as m

from functools import lru_cache


class Model:
    def __init__(self, alpha, beta, phi, h, l):
        self.alpha = alpha
        self.beta = beta
        self.phi = phi
        self.h = h
        self.l = l

    @lru_cache(maxsize=1)  # What is the best maxsize?
    def Y(self, H, K, eta):
        alpha = self.alpha

        intangible = m.pow(H, alpha) * m.pow(self.h, 1 - alpha)
        tangible = m.pow(K, alpha) * m.pow(self.l, 1 - alpha)

        return m.pow(tangible, eta) * m.pow(intangible, 1 - eta)

    def K_prime(self, H, K, eta):
        alpha = self.alpha
        output = self.Y(H, K, eta)

        output_adj = output * alpha * (1 - eta)

        return (output_adj * output * (1 - alpha)) / (output_adj + 1)

    def intangible(self, H, K, eta):
        beta = self.beta
        alpha = self.alpha
        output = self.Y(H, K, eta)

        return m.sqrt(alpha * beta * eta * output) / beta

    def equilibrium(self, H, K, eta, p):
        return (1 - self.alpha) - (p + K)*self.Y(H, K, eta)
