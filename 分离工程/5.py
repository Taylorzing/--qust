import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import show,plot
from numpy import linspace
from sympy import symbols, diff
#The composition and equilibrium constants of a vapor mixture are as follows:
y=[0.35,0.2,0.45] #露点
P=2    #P:2Mpa  t:C
t=symbols("t")
K=[0.15*t/P,0.02*t/P,0.45*t/P]
F=-1
for i in range(len(y)):
    f=y[i]/K[i]
    F+=f
    # print(f)
# print(F)
def dawfunc():
    tt = linspace(1, 35)
    yy = []
    for t in tt:
        yy.append(F.subs(symbols("t"), t))
    # print(tt, "\n", yy)
    plot([0,35],[1,1])
    plt.plot(tt, yy)
    plt.show()

def Newton(f,x0=10, epsilon=1/10**4, iternum=100000):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    fdx = diff(f, t)
    for i in range(iternum):
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
Newton(f=F-1)
dawfunc()