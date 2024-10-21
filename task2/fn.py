# EPS = 0.00000000001


def left_rectangle(f, xi, xj):
    assert xi < xj

    return f(xi) * (xj - xi)


def central_rectangle(f, xi, xj):
    assert xi < xj

    x = (xi + xj) / 2

    return f(x) * (xj - xi)


def trapezoid(f, xi, xj):
    assert xi < xj

    sy = f(xi) + f(xj)
    dx = xj - xi

    return sy * dx / 2


def simpson(f, xi, xj):
    assert xi < xj

    xc = (xi + xj) / 2
    dx = (xj - xi)

    r = f(xi) + f(xc) * 4 + f(xj)

    return r * dx / 6


def newton2(f, xi, xj):

    p = (xi + xj) / 2
    q = (xi - xj) * (3 ** 0.5) / 6

    r = f(p + q) + f(p - q)

    return r * (xj - xi) / 2


def newton3(f, xi, xj):
    p = (xi + xj) / 2
    q = (xj - xi) / 2

    x1 = -0.774596669240
    x3 = -x1

    y1 = p + q * x1
    y3 = p + q * x3
    y2 = p

    r = f(y1) * 5 + f(y2) * 8 + f(y3) * 5
    r = r * q / 9

    return r


def split(N, a, b):
    assert a < b
    assert N > 0

    X = [a]

    s = a
    dx = (b - a) / N

    for _ in range(N - 1):
        s += dx 
        X.append(s)

    X.append(b)

    return X


def create_table(fns):
    return [list(fns.keys())]


def calc(cols, fns, F, N, X, t=None):
    Y = []

    for key in cols:
        s = 0

        for i in range(N):
            s += fns[key](F, X[i], X[i + 1])

        if t is None:
            Y.append(s)
        else:
            Y.append(abs(s - t))

    return Y


def power(d1, d2):
    assert len(d1) == len(d2)

    R = []

    for i in range(len(d1)):
        # if (abs(d2[i]) < EPS):
        #     R.append(-1)
        # else:
        R.append(d1[i] / d2[i])

    return R

# В работе
def improve(table, i, j, p):
    d1 = table[i]
    d2 = table[j]

    R = [0] * len(d1)

    for i in range(len(d1)):
        a = -1 / (2 ** p[table[0][i]] - 1)
        R[i] = a * d1[i] + (1 - a) * d2[i]

    return R


def print_table(table, tLen=10, tabs=[]):
    N = len(table) - 1

    tabs += [4] * (N - len(tabs))

    for i in range(len(table[0])):
        print(("{:" + str(tLen) +  "s}\t").format(table[0][i]), end="")

        for j in range(1, len(table)):
            print(("{:8." + str(tabs[j - 1]) + "f}\t").format(table[j][i]), end="")
        
        print()
