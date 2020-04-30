from numpy import array as vector


def seir_model(beta, gamma, a):
    def f(t, x):
        S, E, I, R = x
        return vector([
            -beta*S*I,
            beta*S*I - a*E,
            a*E - gamma*I,
            gamma*I
        ])
    return f
