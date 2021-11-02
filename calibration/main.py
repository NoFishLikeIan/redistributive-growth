from dotenv import load_dotenv
import numpy as np
from solver import naive
from model import Model
import os

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['figure.figsize'] = (12, 9)
matplotlib.rcParams['figure.dpi'] = 200


load_dotenv()


plot_path = os.environ.get("PLOT_PATH", ".")

# default parameters

if __name__ == "__main__":
    m = Model(
        alpha=0.4,
        beta=1,
        phi=0.3,
        h=24.438,
        l=15.945
    )

    H, K = 3., 8.
    Ys = np.linspace(5., 10., num=100)

    etas = np.empty(Ys.shape)
    errors = np.empty(Ys.shape)

    for t, Y in enumerate(Ys):

        eta, error = naive.get_eta(m, Ys[t], H, K)
        etas[t] = eta
        errors[t] = error

    fig, (ax_eta, ax_error) = plt.subplots(2, 1, sharex=True)
    ax_eta.plot(Ys, etas)
    ax_eta.set_title(r'Solution to $\eta$')
    ax_eta.set_ylabel(r'$\eta$')

    ax_error.plot(Ys, errors)
    ax_error.axhline(0., linestyle='--', color='black')
    ax_error.set_ylabel('Equilibrium squared error')
    ax_error.set_xlabel(r'$Y$')

    fig.savefig(os.path.join(plot_path, "naive_sol_eta.png"))
