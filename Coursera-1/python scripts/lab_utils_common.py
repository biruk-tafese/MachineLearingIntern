# lab_utils_common.py
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for color dictionary
dlc = {"dlblue": "blue"}

# Placeholder for plot_data function
def plot_data(X, y, ax):
    """
    Scatter plot of training data.

    Args:
        X (ndarray): Shape (m, 2) - Input features (two variables)
        y (ndarray): Shape (m,) - Labels (0 or 1)
        ax (matplotlib.axes._subplots.AxesSubplot): Axis for the plot
    """
    pos = y == 1
    neg = y == 0

    ax.scatter(X[pos, 0], X[pos, 1], marker='x', s=80, c='red', label="y=1")
    ax.scatter(X[neg, 0], X[neg, 1], marker='o', s=100, label="y=0", facecolors='none',
               edgecolors=dlc["dlblue"], lw=3)

    ax.set_ylim(-0.5, 2.5)
    ax.set_xlim(-0.5, 3.5)
    ax.set_xlabel('$x_0$', fontsize=12)
    ax.set_ylabel('$x_1$', fontsize=12)
    ax.legend()


# plt_one_addpt_onclick.py
import matplotlib.pyplot as plt
import numpy as np

def plt_one_addpt_onclick(X, y):
    """
    Plot data with the ability to add a point on click.

    Args:
        X (ndarray): Shape (m, 2) - Input features (two variables)
        y (ndarray): Shape (m,) - Labels (0 or 1)

    Returns:
        fig (matplotlib.figure.Figure): Figure object
        ax (matplotlib.axes._subplots.AxesSubplot): Axis object
    """
    fig, ax = plt.subplots()
    plot_data(X, y, ax)

    def onclick(event):
        # Implement the logic to add a point on click
        pass

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    return fig, ax
