import matplotlib.pyplot as plt

# Фун. рекурсивно вычисляет разделенную разность по X и Y
# (x_i, ..., x_j), (y_i, ..., y_j)

def divided_difference(i, j, X, Y, hist = None):
    if (hist is None):
        hist = dict()
    
    if (i > j):
        return None
    elif (i == j):
        return Y[i]
    elif ((i, j) in hist):
        return hist[(i, j)]
    
    a = divided_difference(i, j - 1, X, Y, hist)
    b = divided_difference(i + 1, j, X, Y, hist)

    d = (b - a) / (X[j] - X[i])

    if ((i, j) not in hist):
        hist[(i, j)] = d

    return d


# Фун. вычисляет значение коэф. полинома Ньютонa
# по узлам сетки размера n + 1

def newton_interpolation_pcoef(n, X, Y):
    hist, A = dict(), []

    for i in range(0, n + 1):
        A.append(divided_difference(0, i, X, Y, hist))
    
    return A


# Фун. вычисляет значение полинома Ньютона степени n
# с коэф. A в точке x_

def newton_interpolation(x_, n, A, X):
    p, r = 1, 0

    for i in range(n + 1):
        r += p * A[i]
        p *= x_ - X[i]
    
    return r


# 

def linear_interpolation(x_, n, X, Y):
    for i in range(n):
        if (x_ <= X[i + 1] and x_ >= X[i]):
            d = (Y[i + 1] - Y[i]) / (X[i + 1] - X[i])
            return Y[i] + (x_ - X[i]) * d
    
    if (x_ < X[0]):
        return Y[0]
    
    return Y[-1]

# 

def grid(a, b, n):
    r = []
    for i in range(n):
        r.append(a + (b - a) * i / n)
    return r


# 

def calc(f, X):
    r = []
    for i in range(len(X)):
        r.append(f(X[i]))
    return r


#

def plot(f, a, b, n = 200):
    X = grid(a, b, n)
    Y = calc(f, X)

    plt.plot(X, Y)

    return min(Y), max(Y)
