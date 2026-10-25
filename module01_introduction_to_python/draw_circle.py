
import math
import numpy as np
import matplotlib.pyplot as plt

def make_figure():
    theta = np.arange(0, 4 * math.pi, 0.2)
    circle = plt.figure()
    axes = circle.add_axes([0, 0,1,1])
    axes.plot((0.5 * np.sin(theta), np.cos(theta / 2)))
    return circle
