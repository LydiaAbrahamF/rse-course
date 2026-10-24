
import math
import numpy as np
import matplotlib.pyplot as plt

def make_figure():
    theta = np.arange(0, 5 * math.pi, 0.25)
    circle = plt.figure()
    axes = circle.add_axes((0, 0,1,1))
    axes.plot((np.sin(theta), np.cos(theta)))
    return circle
