#! /usr/bin/env python
from sars_cov2.simulation.seir import seir_simulation
from sars_cov2.visualize.diagram import diagram


def simulation1():
    N = 83200000
    R0 = 2.4
    gamma = 1/3.0
    return seir_simulation(beta=R0*gamma, gamma=gamma, a=1/5.5, E0=40000.0/N, I0=10000.0/N, days=140)


if __name__ == '__main__':
    diagram(simulation1)
