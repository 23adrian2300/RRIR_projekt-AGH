import numpy as np

def e(i, x, nof): #funkcja bazowa
    return np.maximum(1 - np.abs((x - i * (2 / nof)) / (2 / nof)), 0)

def e_derivative(i, x,nof): # pochodna funkcji bazowej
    return (np.where(((2 / nof) * (i - 1) <= x) & (x < (2 / nof) * i) & (0 <= x), 1 / (2 / nof), 0) +
            np.where(((2 / nof) * i <= x) & (x < (2 / nof) * (i + 1)) & (x <= 2), -1 / (2 / nof), 0))

