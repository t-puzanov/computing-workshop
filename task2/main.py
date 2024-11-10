import fn, math


def F(x):
    return math.sin(x) + ((x ** 3) * math.sin(x)) ** 2


def main():

    a, b = -math.pi, math.pi

    N = 20

    X1 = fn.split(N * 1, a, b)
    X2 = fn.split(N * 2, a, b)

    t = math.pi ** 7 / 7 - 3 * math.pi * (15 + 2 * (math.pi ** 2) * (math.pi ** 2 - 5)) / 4

    fns = {
        "Left Rectangles": fn.left_rectangle,
        "Central Rectangles": fn.central_rectangle,
        "Trapezoid": fn.trapezoid,
        "Simpson": fn.simpson,
        "Gauss (k=1)": fn.gauss2,
        "Gauss (k=2)": fn.gauss3
    }

    p = {
        "Left Rectangles": 4,
        "Central Rectangles": 4,
        "Trapezoid": 4,
        "Simpson": 4,
        "Gauss (k=1)": 4,
        "Gauss (k=2)": 6
    }

    tLen = max(map(len, fns.keys()))

    table = fn.create_table(fns)
    cols  = table[0]

    c1 = fn.calc(cols, fns, F, N * 1, X1)
    c2 = fn.calc(cols, fns, F, N * 2, X2)

    table.append(fn.calc(cols, fns, F, N * 1, X1, t))
    table.append(fn.calc(cols, fns, F, N * 2, X2, t))

    table.append(fn.power(table[1], table[2]))

    table.append(fn.improve(table, c1, c2, p, t))

    fn.print_table(table, tLen, [15, 15, 2, 15])


if __name__ == "__main__":
    main()
