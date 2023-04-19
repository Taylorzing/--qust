import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

from scipy.misc import derivative
import sympy as sy

P = 1  # 0.1Mpa=1bar
y = [0.05, 0.17, 0.65, 0.10, 0.03]
# x = [0.05, 0.17, 0.65, 0.10, 0.03]
a = [9.0580, 9.2131, 9.2164, 9.2535, 9.3224]
b = [2154.90, 2477.07, 2697.55, 2911.32, 3120.29]
c = [-34.42, -39.94, -48.8, -56.51, -63.63]
t = sy.symbols("t")


def fugacity_coefficient():
    tc = [425.12, 269.7, 507.6, 540.2]  # K  临界温度
    pc = [37.96, 33.7, 30.25, 27.4]  # bar(10^5)  临界压力
    w = [0.200164, 0.251206, 0.301261, 0.349469]  # 偏心因子ω
    pr, tr, fc, B0, B1 = [], [], [], [], []
    for i in range(len(y) - 1):
        pr.append(P / pc[i])
        tr.append(t / tc[i])
        B0.append(0.083 - 0.422 / pow(tr[i], 1.6))
        B1.append(0.139 - 0.172 / pow(tr[i], 4.2))
        fc.append(sy.exp(pr[i] / tr[i])*(B0[i] + w[i] * B1[i]))
    return fc
def activity_coefficient():


fugacity_coefficient()


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


xsum = 0
for i in range(len(y)):
    # f = exp(a[i] + b[i] / t + c[i] * P) * x[i]
    f = y[i] / (sy.exp(a[i] - b[i] / (c[i] + t)) / P)
    print(f)
    xsum += f


# print(xsum)


def dawfunc():
    tt = linspace(300, 450)
    yy = []
    for t in tt:
        yy.append(xsum.subs(symbols("t"), t))
        # func.evalf(subs={'x2': 6})
        # yy.append(ysum.evalf(subs={'t': t}))

    plt.plot([300, 450], [1, 1])
    plt.plot(tt, yy)
    plt.show()


# Newton(x0=1000,f=ysum-1,epsilon=1 / 10 ** 5, iternum=1000)
def xqf(f, a=300, b=499, epsilion=1 / 10 ** 4, iter=3000):
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

# xqf(f=xsum - 1, a=330, b=411, epsilion=1 / 10 ** 10, iter=300)
# Newton(x0=320,f=xsum-1,epsilon=1 / 10 ** 5, iternum=1000)
# dawfunc()
