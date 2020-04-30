from numpy import array as vector

from sars_cov2.math.solver import euler_method
from sars_cov2.model.seir import seir_model


def seir_simulation(beta, gamma, a, E0, I0, days, step=0.1):
    x0 = vector([1.0 - E0 - I0, E0, I0, 0.0])
    return euler_method(seir_model(beta, gamma, a), 0, x0, days, step)
