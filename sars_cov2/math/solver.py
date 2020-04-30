def euler_method(f, t0, x0,t1, h):
    """Explicit Euler method."""
    t = t0
    x = x0
    a = [[t, x]]
    for k in range(0, 1 + int((t1 - t0)/h)):
        t = t0 + k*h
        x = x + h*f(t, x)
        a.append([t, x])
    return a
