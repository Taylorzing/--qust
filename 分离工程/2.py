from matplotlib import pyplot as plt
from numpy import linspace
from scipy import *
from sympy import *
from util import niu_dun

P = 23  # 2.3Mpa=23bar
x = [0.0132, 0.8108, 0.1721, 0.0039]
a = [8.6041, 8.9166, 9.0435, 9.1058]
b = [597.84, 1347.01, 1511.42, 1872.46]
c = [-7.16, -18.15, -17.16, -25.16]
t = symbols("t")
ysum = 0
for i in range(len(x)):
    # f = exp(a[i] + b[i] / t + c[i] * P) * x[i]
    f = x[i] / (exp(a[i] - b[i] / (c[i] + t)) / P)
    # print(f)
    ysum += f


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


def xqf(f, a=200, b=300, epsilion=1 / 10 ** 4, iter=300):
    xa, xb = a, b
    for i in range(iter):
        fa = f.subs(t, xa)
        fb = f.subs(t, xb)
        # fb = f.evalf(f.subs(t, xb))
        x_1 = xb - (fb * (xb - xa) / (fb - fa))
        print(fa, fb)
        print("第", i + 1, "次迭代 ", "xa=", xa, "  x_1=", x_1, "  |xa - xb|=", abs(xa - xb))
        if abs(xb - xa) < epsilion:
            break
        else:
            xa, xb = xb, x_1
    return x_1


def dawfunc():
    yy = []
    tt = linspace(200, 400)
    for i in tt:
        yy.append(ysum.subs(t, i))
    plt.xlabel("t/C")
    # print(tt,yy)
    plt.plot(tt, yy)
    plt.plot([200, 400], [1, 1])
    plt.show()


def richmond(f, x0=100, epsilon=1 / 10 ** 5, iternum=100):
    xk_1 = x0
    fdx = diff(f, t)
    fdx2 = diff(f, t, 2)
    xmin=[]
    for i in range(iternum):

        fx = f.subs(t, xk_1)
        fdx = fdx.subs(t, xk_1)
        fdx2 = fdx2.subs(t, xk_1)

        if fdx != 0:
            xk = xk_1 - 2 / ((2 * fdx / fx) - (2 * fdx2 / fdx))
            print("第", i + 1, "次迭代 ", "xk=", xk, "  xk-1=", xk_1, "  |xk - xk-1|=", abs(xk - xk_1))
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            break
    print("方法失败")
    return xk


# dawfunc()
Newton(x0=200,f=ysum-1)
# xqf(f=ysum - 1)

richmond(f=ysum - 1, x0=250)

