# Packages
import numpy as np

from functools import lru_cache

class Model:
    def __init__(self, alpha, beta, phi, h, l):
        self.alpha = alpha
        self.beta = beta
        self.phi = phi
        self.h = h
        self.l = l

    @lru_cache(maxsize=5)
    def Y(self, H:float, K:float, eta:float) -> float:
        """
        Compute output given a intangible stock H, a tangible stock K, and a relative productivity eta
        """

        alpha = self.alpha
        intangible = np.power(H, alpha) * np.power(self.h, 1 - alpha)
        tangible = np.power(K, alpha) * np.power(self.l, 1 - alpha)

        return np.power(intangible, eta) * np.power(tangible, 1 - eta)

    def K_prime(self, H:float, K:float, eta:float) -> float:
        """
        Compute derivative of capital given an intangible stock H, a tangible stock K, and a relative productivity eta
        """

        output = self.Y(H, K, eta)

        num = self.alpha * (1 - self.alpha) * (1 - eta) * np.square(output)
        den = self.alpha * (1 - eta) * output + 1
        
        return num / den

    def K_next(self, H:float, K:float, eta:float) -> float:
        pass

class Model(Model):

    def __init__(self):
        pass


    def new_capital(eta , output):
        numerator = alpha*(1−alpha)*(1−eta)*output**2 denominator = alpha*(1−eta)*output + 1

# Parameter space eta_0 = 0.3 eta_end = 0.85 alpha = 0.4
alpha = 0.
beta = 1
phi = 0.3
# labour
h = 24.438 
l = 15.945
# Starting values H_0 = 0.973
K_0 = 3.259
# Number of Runs num_run = 150000 endtime = 110000
# Defining variables


def new_capital(eta , output):
numerator = alpha*(1−alpha)*(1−eta)*output**2 denominator = alpha*(1−eta)*output + 1
return numerator/denominator
def intang_cap ( eta , output , beta ) :
return math.sqrt(alpha*beta*eta*output)/beta
def equil(Y, p, K):
return (1−alpha) − pY − KY
# Defining H and K
H = H_0 K = K_0
# Assigning and Appending
outputs = [] Hs = [H_0] Ks = [K_0] rs=[]
ws = [] ps = [] Ms = []
MMs = [] MPs = [] Mws = [] KYs = []
88
HRs = [] Rs = [] HRYs = []
# Main
eta = eta_0 etas = []
for i in range(num_run):
KY r = R =
w =
HR = H*R
HRY = HR/Y
pY = 1/(r*Y)
MY = max(0, (1 − phi) * (pY) − (1 − alpha) * (1 − eta))
M = max(0, (1 − phi) * (pY*Y) − (1 − alpha) * (1 − eta)* Y) MP = M/(pY * Y)
Mw=M/(w* l)
# Eta process
if i > 10000 and i < endtime:
eta = eta + (eta_end−eta_0)/(endtime−10001) #print ( eta )
# Appending
outputs .append(Y) Hs . append (H) Ks.append(K)
r s . append ( r )
ws . append (w) ps . append ( pY ) Ms.append(MY)
MMs.append(M) MWs.append(MW) MPs.append(MP)
KYs.append(KY) HRs.append(HR) Rs . append ( R ) HRYs.append(HRY)