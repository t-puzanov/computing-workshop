import matplotlib.pyplot as plt
import fn, math


def f1(x):
    return x * math.sin(x)

def f2(x):
    return x * x * x

def f3(x):
    if (x < 0):
        return x * 0.5
    else:
        return x * x
    

def main():
    
    a, b = -math.pi * 10, math.pi * 10

    F = f1

    N, step = 30, 1000

    X = [0] * (N + 1)
    Y = [0] * (N + 1)

    for i in range(N + 1):
        X[i] = (a + (b - a) * i / (N + 1)) 
    
    for i in range(N + 1):
        Y[i] = F(X[i])

    coef = fn.newton_interpolation_pcoef(N, X, Y)

    ymin, ymax = fn.plot(lambda x: F(x), a, b, step)

    fn.plot(lambda x: fn.newton_interpolation(x, N, coef, X), a, b, step)
    # fn.plot(lambda x: fn.linear_interpolation(x, N, X, Y), a, b, step)

    plt.legend(['φ(x)', 'f(x)'])

    plt.plot(X, Y, 'ro')

    plt.axis([a, b, ymin, ymax])

    plt.show()


if __name__ == "__main__":
    main()
