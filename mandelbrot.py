import os
import sys
import time

import numpy as np


def mandelbrot(exp):

    max = 4
    it = 10

    x_axis = [_ * 0.05 for _ in range(-max * 7, max * 7)]
    y_axis = [_ * 0.05 for _ in range(-max * 10, max * 10)]

    def z(x, c, exp):
        return (x**exp) + c

    out = ""

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

        out += f"{conc}\n"

    print(out, f"printing [ Z=Z^N + C ] with N = {exp}")


def main():

    exp = 2
    iterate = False

    if len(sys.argv) > 1:

        if sys.argv[1] == "-i" or sys.argv[1] == "--iterate":
            iterate = True
            exp = float(sys.argv[2])
        else:
            exp = float(sys.argv[1])

    if iterate:
        step = 0.05
        arr = np.arange(0, exp + step, step)
        
        os.system("cls" if sys.platform == 'win32' else "clear")

        for i in arr:
            mandelbrot(i)
            #time.sleep(0.001)

            if i != arr[-1]:
                print("\x1b[H")

    else:
        mandelbrot(exp)


if __name__ == '__main__':
    main()
