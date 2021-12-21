from pandas import DataFrame

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Defaults
matplotlib.rcParams['text.usetex'] = True
sns.set_theme(
    style = "whitegrid", font_scale=1.25, 
    rc = {"figure.figsize": (12, 9), "figure.dpi": 200}
)

def plotresults(results:DataFrame):

    years = [date.year for date in results.index]

    fig, ax_eta = plt.subplots()
    ax_eta.set_title(r'Solution to $\eta$')
    ax_eta.set_xlabel('Time')
    ax_eta.set_xticks(years)

    color = 'tab:red'
    ax_eta.plot(years, results.eta, '-o', color = color)
    ax_eta.set_ylabel(r'$\eta$', color = color, rotation = 0)

    ax_beta = ax_eta.twinx()

    color = 'tab:blue'
    ax_beta.plot(years, results.beta, '-o', color = color)
    ax_beta.set_ylabel(r'$\beta$', color = color, rotation = 0)

    fig.tight_layout()
    
    return fig