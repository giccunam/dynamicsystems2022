#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Variable for maximum level
MAX_LEVEL = 6

def triangle(x, y, mu, l, s):
    """Returns the coordinates of an equilateral triangle as a numpy array
    with two elements: all x values, and all y values.

    Parameters:
    x, y (floats):  Coordinates of the midpoint of the base of the triangle.
    mu (float):     Slope of the base of the triangle.
    l (float):      Length of the base of the triangle.
    s (int):        Defines direction of the triangle (-1: down, 1: up).
    """

    theta = np.arctan(mu)
    n = s * np.sqrt(l**2 - (l/2)**2)

    Q1 = np.array([x-l/2*np.cos(theta), y-l/2*np.sin(theta)])
    Q2 = np.array([x+l/2*np.cos(theta), y+l/2*np.sin(theta)])
    Q3 = np.array([x-n*np.sin(theta), y+n*np.cos(theta)])

    return np.array([[Q1[0], Q2[0], Q3[0], Q1[0]], [Q1[1], Q2[1], Q3[1], Q1[1]]])

def compute_coordinates(x, y, l, mu, x_Q1, y_Q1, x_Q2, y_Q2, x_Q3, y_Q3):
    """Given an input triangle, return the coordinates for the three smaller
    triangles attached to each side of the input triangle.
    """

    # Length and slope of each triangle base
    li = l / 3.0
    m1 = (y_Q3 - y_Q1) / (x_Q3 - x_Q1)
    m2 = (y_Q3 - y_Q2) / (x_Q3 - x_Q2)
    m3 = mu

    # Coordinates of r1
    x_r1 = (x_Q1 + x_Q3) * 0.5
    y_r1 = (y_Q1 + y_Q3) * 0.5

    # Coordinates of r2
    x_r2 = (x_Q3 + x_Q2) * 0.5
    y_r2 = (y_Q3 + y_Q2) * 0.5

    # Coordinates of r3
    x_r3 = x
    y_r3 = y

    return li, m1, m2, m3, x_r1, y_r1, x_r2, y_r2, x_r3, y_r3

def fractal(n, ax, x, y, mu, l):
    """Generates a fractal recursively.
    """

    if n > 0:
        X, Y = triangle(x, y, mu, l, 1)
        ax.plot(X,Y)
        (l1, m1, m2, m3, x_r1, y_r1,
        x_r2, y_r2, x_r3, y_r3) = compute_coordinates(x, y, l, mu, X[0], Y[0],
                                                      X[1], Y[1], X[2], Y[2])
        fractal(n-1,ax, x_r1, y_r1,m1,l1)
        fractal(n-1,ax, x_r2, y_r2,m2,l1)

        if n == MAX_LEVEL:
            fractal(n-1,ax, x_r3, y_r3,m3,l1)

if __name__ == '__main__':
    """Driver code."""

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    # Initial conditions
    x, y, mu, l = 0, 0, 0, 1

    # Fractal generation
    fractal(6, ax, x, y, mu, l)

    # X, Y = triangle(x, y, mu, l, 1)
    # ax.plot(X, Y)

    # Next iteration
    # l1 = l / 3
    # m1 = (Y[2] - Y[0]) / (X[2] - X[0])
    # m2 = (Y[2] - Y[1]) / (X[2] - X[1])
    # m3 = mu
    #
    # x_r1 = (X[0] + X[2]) * 0.5
    # y_r1 = (Y[0] + Y[2]) * 0.5
    #
    # x_r2 = (X[2] + X[1]) * 0.5
    # y_r2 = (Y[2] + Y[1]) * 0.5
    #
    # x_r3 = x
    # y_r3 = y

    # (l1, m1, m2, m3,
    # x_r1, y_r1, x_r2, y_r2,
    # x_r3, y_r3) = compute_coordinates(x, y, l, mu, X[0], Y[0], X[1], Y[1],
    #                                   X[2], Y[2])
    # X, Y = triangle(x_r1, y_r1, m1, l1, 1)
    # ax.plot(X, Y)
    # X, Y = triangle(x_r2, y_r2, m2, l1, 1)
    # ax.plot(X, Y)
    # X, Y = triangle(x_r3, y_r3, m3, l1, -1)
    # ax.plot(X, Y)

    plt.show()
