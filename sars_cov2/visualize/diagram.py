import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot


def diagram(simulation):
    plot.style.use('fivethirtyeight')
    figure, axes = plot.subplots()
    figure.subplots_adjust(bottom=0.15)
    #axes.gridaxes.grid(linestyle=':', linewidth=2.0, color="#808080")
    t, x = zip(*simulation())
    S, E, I, R = zip(*x)
    axes.plot(t, S, color="#0000cc")
    axes.plot(t, E, color="#ffb000", linestyle='--')
    axes.plot(t, I, color="#a00060")
    axes.plot(t, R, color="#008000", linestyle='--')
    plot.show()
