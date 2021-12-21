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

def estimate_data(data, verbose = False, beta = None):
    compute_beta = beta is None

    N = len(data)
    params = 2 if compute_beta else 1

    parameters = np.empty((N, params))
    errors = np.empty((N,))

    for i, f in data.iterrows():    
        if verbose: print(f"Working on year: {f.sasdate} \r")    
        
        m = Model(alpha=f.alpha, phi=f.phi, h=f.h, l=f.l)

        if compute_beta:
            params, error = naive.get_parameters(m, f.Y, f.H, f.K)
            parameters[i, :] = params
        else:
            params, error = naive.get_eta(m, f.Y, f.H, f.K, beta = beta)
            parameters[i] = params

        errors[i] = error

    cols = ["eta", "beta"] if compute_beta else ["eta"]
    result = pd.DataFrame(parameters, columns = cols, index = data.sasdate)
    result["errors"] = errors

    return result

if __name__ == "__main__":
    data = pd.read_csv("data/calibration_data.csv")
    data.sasdate = data.sasdate.apply(pd.to_datetime)

    results = estimate_data(data)
    print(results)

