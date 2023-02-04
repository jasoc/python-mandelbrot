import os
import random
import sys
import time

import numpy as np

def mandelbrot(exp):
    max = 4
    it = 10
    chardnum = 2
    chararr = '£$%&ç@#*+?'
    x_axis = [_ * 0.05 for _ in range(-max * 7, max * 7)]
    y_axis = [_ * 0.05 for _ in range(-max * 10, max * 10)]
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
                    res = calc(res, c, exp)
                if abs(res) >= max:
                    break
            if abs(res) <= max / 2:
                conc += f"{random.choice(chararr)}" * chardnum
            else:
                conc += " " * chardnum
        out += f"{conc}\n"
    print(out, f"printing [ Z=Z^N + C ] with N = {str(exp)[0:4] if exp < 10 else str(exp)[0:5]}")

def calc(x, c, exp):
    return (x**exp) + c

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
        arr = np.arange(1, exp + step, step) 
        try:
            for i in arr:
                mandelbrot(i)
                if i > 1 and i < 8 and round(i, 2).is_integer():
                    time.sleep(1)
                elif i <= 3:
                    time.sleep(0.03)
                else:
                    time.sleep(0.01)
                if i != arr[-1]:
                    print("\x1b[H")
        except KeyboardInterrupt:
            print("\x1b[H")
            os.system("cls" if sys.platform == 'win32' else "clear")
    else:
        mandelbrot(exp)

if __name__ == '__main__':
    main()
