from matplotlib import pyplot as plt
from matplotlib.pyplot import show
from numpy import linspace
from sympy import *
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
z = [0.1, 0.2, 0.3, 0.4]
a = [9.1058, 9.0825, 9.2131, 9.2164]
b = [1872.46, 2154.90, 2477.07, 2697.55]
c = [-25.16, -34.42, -39.94, -48.78]
T, P = 366.5, 6.895  # 366.5K  689.5Kpa=6.895bar

K = []
t = T
zk = 0
for i in range(4):
    K.append(exp(a[i] - (b[i] / (c[i] + t))) / P)  # 安托因方程求相平衡常数
    zk += (z[i] / K[i])  # 1.86>1 可以进行闪蒸
# print(K,zk)
v = symbols("v")
Fv = 0
for i in range(4):
    f = z[i] * (K[i] - 1) / (1 + v * (K[i] - 1))
    Fv += f
    # print(Fv)


def dawfunc():
    vv = linspace(0, 1, 100)
    yy = []
    for v in vv:
        yy.append(Fv.subs(symbols("v"), v))
    plt.grid()
    plt.xlabel("气化率/v")
    plt.plot([0,1],[0,0])
    plt.plot(vv, yy)
    plt.show()

def Newton(f, v0=0.5, epsilon=1 / 10 ** 10, iternum=100):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = v0
    fdx = f.diff(v)
    for i in range(iternum):
        fx = f.subs(v, xk_1)
        fdx = fdx.subs(v, xk_1)
        if fdx != 0:
            xk = xk_1 - fx / fdx
            print("第", i + 1, "次迭代 ", "xk=", xk, "  xk-1=", xk_1, "  |xk - xk-1|=", abs(xk - xk_1), "下降f/df：",
                  fx / fdx);
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            break
    print("方法失败")
    return 0

Newton(Fv)
dawfunc()