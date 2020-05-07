# coding=utf-8


def euler_method(f, t0, x0, t1, h):
    """Explizites Euler-Verfahren.
    Einfachstes Verfahren zur numerischen Lösung eines Anfangswertproblems
        x' = f(t, x), x(t0) = x0
    durch Berechnung von
        tk = t0 + k*h, k = 0, 1, 2, ...
        xk+1 = xk + h*f(tk, xk), k + 0, 1, 2, ...

    :param f: zu lösendes Anfangswertproblem x' = f(t, x), x(t0) = x0
    :param t0: Anfangs-Zeitpunkt t0
    :param x0: Anfangswert x0
    :param t1: End-Zeitpunkt t1
    :param h: Diskretisierungs-Schrittweite h > 0
    :return: Liste von Approximationen an den diskreten Zeitpunkten k
    """
    t = t0
    x = x0
    approx = [[t, x]]
    for k in range(0, 1 + int((t1 - t0)/h)):
        t = t0 + k*h
        x = x + h*f(t, x)
        approx.append([t, x])
    return approx
