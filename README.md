# Python Mandelbrot
### A simple python script that print the Mandelbrot set for every power of the formal formula.

```
                                                                        **


                                                                            **
                                                                          ****
                                                                      **  ****  **
                                                                        **********
                                                                      ************
                                                                        ********
                                                          ****    **********************      **
                                                          ******************************  **  **
                                                          ************************************
                                                      **  **************************************
                                                    ******************************************
                                                      ******************************************
                                                    **********************************************
                                ****  ******        **********************************************
                                ****************    ********************************************
                                ******************************************************************
                        **    ********************************************************************
                          **********************************************************************
                        **********************************************************************
    **  **  **      ************************************************************************
                        **********************************************************************
                          **********************************************************************
                        **    ********************************************************************
                                ******************************************************************
                                ****************    ********************************************
                                ****  ******        **********************************************
                                                    **********************************************
                                                      ******************************************
                                                    ******************************************
                                                      **  **************************************
                                                          ************************************
                                                          ******************************  **  **
                                                          ****    **********************      **
                                                                        ********
                                                                      ************
                                                                        **********
                                                                      **  ****  **
                                                                          ****
                                                                            **


                                                                        **
```

### If you don't see the set printed, zoom out your terminal.

---

The standard formula for the set is
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^2 + c">

However, the script is generalized for every power, so basically can calculate
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^N + c">
for every N.

If you execute the script as is, it will print the set calculated with N=2, but you can pass as a console argument every N you want.

Example:
```bash
mandelbrot.py 4
```
will print
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^4 + c">

If you pass the ```-i``` or ```--iterate``` parameter, it will print print all the power until will reach the passed one.
So

```bash
mandelbrot.py --iterate 3
```

will print
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^1 + c">
then
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^2 + c">
and
<img src="https://render.githubusercontent.com/render/math?color=white&math=z = z^3 + c">

Install dependencies with ```pip install -r requirements.txt```
#### And sorry for some dumb math trick inside the code :monkey_face:
