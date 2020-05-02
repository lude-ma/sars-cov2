# coding=utf-8
from numpy import array as vector


def seir_model(beta, gamma, a):
    """SEIR-Modell.
    Beschreibt eine Population von N Individuen als
        NS + NE + NI + NR = N
    mit
        S: Anteil der Anfälligen. Noch nicht infiziert. (engl. susceptible)
        E: Anteil der Exponierten. Infiziert aber noch nicht infektiös.
           (engl. exposed)
        I: Anteil der Infektiösen. (engl. infectious)
        R: Anteil der Erholten oder Verstorbenen. (engl. recovered/resistant)

    :param beta: Transmissionsrate (Kontaktrate) [1/d]. Der Kehrwert ist die
                 mittlere Zeit zwischen Kontakten.
    :param gamma: Gesundungsrate [1/d]. Der Kehrwert ist die mittlere
                  infektiöse Zeit.
    :param a: Der Kehrwert ist die mittlere Latenzzeit [1/d]. Die mittlere
              Latenzzeit ist die durchschnittliche Zeit, die ein Individuum in
              der Gruppe E der Exponierten verbringt. Diese ist zu
              unterscheiden von der mittleren Inkubationszeit, denn der Beginn
              der Infektiösität muss nicht mit dem Beginn der Symptome
              übereinstimmen.
    :return: Nichtlineares System gewöhnlicher Differentialgleichungen.
    """
    def f(t, x):
        S, E, I, R = x
        return vector([
            -beta*S*I,
            beta*S*I - a*E,
            a*E - gamma*I,
            gamma*I
        ])
    return f
