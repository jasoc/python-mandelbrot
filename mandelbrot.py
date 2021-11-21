import os
import sys
import time


def mandelbrot(exp):

    max = 4
    it = 10

    x_axis = [_ * 0.05 for _ in range(-max*7, max*7)]
    y_axis = [_ * 0.05 for _ in range(-max*10, max*10)]

    def z(x, c, exp):
        return (x ** exp) + c

    for x in x_axis:

        conc = ""

        for y in y_axis:

            c = complex(y, x)
            res = 0

            for i in range(it):

                if i == 0:
                    res = c
                else:
                    res = z(res, c, exp)

                if abs(res) >= 100:
                    break

            if abs(res) <= 1:
                conc += "**"
            else:
                conc += "  "

        print(conc)


def main():

    exp = 2
    iterate = False

    if len(sys.argv) > 1:

        if sys.argv[1] == "-i" or sys.argv[1] == "--iterate":
            iterate = True
            exp = int(sys.argv[2])
        else:
            exp = int(sys.argv[1])

    if iterate:
        for i in range(exp + 1):
            mandelbrot(i)
            time.sleep(0.15)

            if i != exp:
                os.system('cls')
    else:
        mandelbrot(exp)


if __name__ == '__main__':
    main()
