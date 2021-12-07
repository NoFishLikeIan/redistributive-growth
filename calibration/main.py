from solver import naive
from model import Model


import numpy as np
import pandas as pd

# Plotting

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['figure.figsize'] = (12, 9)
matplotlib.rcParams['figure.dpi'] = 200

import seaborn as sns
sns.set()

# Environment

import os
from dotenv import load_dotenv
load_dotenv()
plot_path = os.environ.get("PLOT_PATH", ".")

if __name__ == "__main__":
    data = pd.read_csv("data/calibration_data.csv")

    etas = []
    errors = []

    for _, f in data.iterrows():
        # FIXME: is it constant?
        m = Model(alpha=0.4, beta=1, phi=f.phi, h=f.h, l=f.l)

        eta, error = naive.get_eta(m, f.Y, f.H, f.K)

        etas.append(eta)
        errors.append(error[0])


    etas = np.array(etas)
    errors = np.array(errors)

    years = [pd.to_datetime(s).year for s in data.sasdate]
   
    fig, ax_eta = plt.subplots()
    ax_eta.set_title(r'Solution to $\eta$')
    ax_eta.set_xlabel('Time')
    ax_eta.set_xticks(years)

    color = 'tab:red'
    ax_eta.plot(years, etas, color = color)
    ax_eta.set_ylabel(r'$\eta$', color = color)

    ax_phi = ax_eta.twinx()
    
    color = 'tab:blue'
    ax_phi.plot(years, data.phi, color = color)
    ax_phi.set_ylabel(r'$\phi$', color = color)

    fig.tight_layout()
    fig.savefig(os.path.join(plot_path, "naive_sol_eta.png"))