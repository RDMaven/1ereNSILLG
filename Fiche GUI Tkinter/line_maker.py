

def x_lines_maker(n, zoom):
    xx = []
    x = [c*20 for c in range(n)]
    for i in range(len(x)):
        xx += [zoom* x[i], 0, zoom* x[i], zoom* 440, zoom* (x[i]+10), zoom* 440, zoom* (x[i]+10), 0 ]
    return xx


def y_lines_maker(n,zoom):
    y = [c*20 for c in range(n)]
    yy = []
    for i in range(len(y)):
        yy += [0, zoom* y[i], zoom* 440, zoom* y[i], zoom* 440, zoom* (y[i]+10), 0, zoom* (y[i]+10) ]
    return yy


print(f"self.y_lines = {x_lines_maker(12,2)}\n")
print(f"self.x_lines = {y_lines_maker(22,2)}")