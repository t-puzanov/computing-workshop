import fn, math


def F(x):
    return (x ** 3) * math.sin(x)


def main():

    a, b = 0, math.pi * 10

    N = 20

    X1 = fn.split(N * 1, a, b)
    X2 = fn.split(N * 2, a, b)

    t = 20 * math.pi * (3 - 50 * (math.pi ** 2))

    fns = {
        "Left Rectangles": fn.left_rectangle,
        "Central Rectangles": fn.central_rectangle,
        "Trapezoid": fn.trapezoid,
        "Simpson": fn.simpson
    }

    tLen = max(map(len, fns.keys()))

    table = fn.create_table(fns)
    cols  = table[0]

    table.append(fn.calc(cols, fns, F, N * 1, X1, t))
    table.append(fn.calc(cols, fns, F, N * 2, X2, t))

    table.append(fn.power(table[1], table[2]))

    fn.print_table(table, tLen, [5, 5, 2])


if __name__ == "__main__":
    main()
