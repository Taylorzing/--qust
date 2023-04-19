from scipy import *
from sympy import *
import numpy as np
import util
x = [0.05, 0.3, 0.65]
t = symbols("t")
K = [0.1333 * t + 4.6667, 0.6667 * t + 1.3333, 0.02857 * t + 0.08571]
Y = -1
for i in range(0, len(x)):
    y = x[i] * K[i]
    Y += y
def Newton(x0, epsilon, f,iternum=100):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    fdx = diff(f, t)
    for i in range(iternum):
        # fx = f(xk_1)
        # fdx = derivative(f, xk_1, dx=1e-6)
        fx=f.subs(t,xk_1)
        fdx=fdx.subs(t,xk_1)
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
Newton(30,1/10**4,f=Y)

