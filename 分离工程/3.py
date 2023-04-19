import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from sympy import *
from scipy.misc import derivative

P = 1  # 0.1Mpa=1bar
x = [0.05, 0.17, 0.65, 0.10, 0.03]
a = [9.0580, 9.2131, 9.2164, 9.2535, 9.3224]
b = [2154.90, 2477.07, 2697.55, 2911.32, 3120.29]
c = [-34.42, -39.94, -48.8, -56.51, -63.63]
t = symbols("t")


def Newton(x0, f, epsilon=1 / 10 ** 5, iternum=100):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    fdx = diff(f, t)
    for i in range(iternum):
        # fx = f(xk_1)
        # fdx = derivative(f, xk_1, dx=1e-6)
        fx = f.subs(t, xk_1)

        fdx = fdx.subs(t, xk_1)
        if fdx != 0:
            xk = xk_1 - fx / fdx
            print("第", i + 1, "次迭代 ", "xk=", xk, "  xk-1=", xk_1, "  |xk - xk-1|=", abs(xk - xk_1));
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            break
    print("方法失败")
    return 0


ysum = 0
for i in range(len(x)):
    # f = exp(a[i] + b[i] / t + c[i] * P) * x[i]
    f = (exp(a[i] - b[i] / (c[i] + t)) / P) * x[i]
    print(f)
    ysum += f

print(ysum)


def dawfunc():
    tt = linspace(100, 650)
    yy = []
    for t in tt:
        yy.append(ysum.subs(symbols("t"), t))
        # func.evalf(subs={'x2': 6})
        # yy.append(ysum.evalf(subs={'t': t}))

    plt.plot(tt, yy)
    plt.show()


# Newton(x0=1000,f=ysum-1,epsilon=1 / 10 ** 5, iternum=1000)
def xqf(f, a=300, b=499, epsilion=1 / 10 ** 4, iter=3000):

    xa, xb = a, b
    for i in range(iter):

        print(i)
        # print("-----------%f-----" % (f.subs(t, xb)))
        fa = f.subs(t, xa)
        fb=f.subs(t, xb)
        # fb = f.evalf(f.subs(t, xb))
        x_1 = xb - (fb * (xb - xa) / (fb - fa))
        print(fa,fb)
        print("第", i + 1, "次迭代 ", "xa=", xa, "  x_1=", x_1, "  |xa - xb|=", abs(xa - xb))
        if abs(xb - xa) < epsilion:
            print(xa, xb)
            break
        else:
            xa, xb = xb, x_1
    return x_1


xqf(f=ysum - 1, a=330, b=411, epsilion=1 / 10 ** 10, iter=300)
Newton(x0=1000,f=ysum-1,epsilon=1 / 10 ** 5, iternum=1000)
dawfunc()

