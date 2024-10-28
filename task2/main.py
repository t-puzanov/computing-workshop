import fn, math


def F(x):
    return (x ** 3) * math.sin(x)


def main():

    a, b = 0, math.pi / 2

    N = 20

    X1 = fn.split(N * 1, a, b)
    X2 = fn.split(N * 2, a, b)

    t = (math.pi ** 2 - 8) * 3 / 4

    fns = {
        "Left Rectangles": fn.left_rectangle,
        "Central Rectangles": fn.central_rectangle,
        "Trapezoid": fn.trapezoid,
        "Simpson": fn.simpson,
        "Newton (n=1)": fn.newton2,
        "Newton (n=2)": fn.newton3
    }

    p = {
        "Left Rectangles": 1,
        "Central Rectangles": 2,
        "Trapezoid": 2,
        "Simpson": 4,
        "Newton (n=1)": 4,
        "Newton (n=2)": 6
    }

    tLen = max(map(len, fns.keys()))

    table = fn.create_table(fns)
    cols  = table[0]

    d1 = fn.calc(cols, fns, F, N * 1, X1)
    d2 = fn.calc(cols, fns, F, N * 2, X2)

    table.append(fn.calc(cols, fns, F, N * 1, X1, t))
    table.append(fn.calc(cols, fns, F, N * 2, X2, t))

    table.append(fn.improve(table, d1, d2, p, t))

    table.append(fn.power(table[1], table[2]))

    fn.print_table(table, tLen, [15, 15, 15, 2])


if __name__ == "__main__":
    main()
