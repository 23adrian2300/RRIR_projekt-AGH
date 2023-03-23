from scipy.integrate import fixed_quad, quad
import numpy as np
from Function_e import e_derivative, e


def B(i, j, s, z, nof): # Obliczenie wartości B(ei,ej)
    result, _ = fixed_quad(lambda x: e_derivative(i, x, nof) * e_derivative(j, x,nof), s, z, n=200)
    result -= e(i, 0, nof) * e(j, 0,  nof)
    return result


def k(x): # Funkcja k
    return np.where((x < 0) | (x > 2), 0, np.where(x <= 1, x+1, 2*x))


def L(i, s, z, nof): # Obliczenie wartość L(ei)
    result, _ = quad(lambda x: 100 * x * e(i, x, nof) / k(x), s, z)
    result -= 20 * e(i, 0, nof)
    return result
