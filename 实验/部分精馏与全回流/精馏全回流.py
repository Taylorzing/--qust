import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from scipy.interpolate import make_interp_spline
from scipy.optimize import curve_fit
from scipy.linalg import solve
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# matplotlib.rcParams['text.usetex'] = True
# np.set_printoptions(suppress=True)                                                                    ·
from sympy import *
from pylab import *
import math
import sympy as sp
import math
import numpy as np

x = np.array(
    [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.14, 0.18, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75,
     0.8, 0.85, 0.894, 0.9, 0.95, 1])
y = np.array(
    [0, 0.11, 0.175, 0.273, 0.34, 0.392, 0.43, 0.482, 0.513, 0.525, 0.551, 0.575, 0.595, 0.61, 0.635, 0.657, 0.678,
     0.698, 0.725, 0.755, 0.785, 0.82, 0.855, 0.894, 0.898, 0.942, 1])
print(len(x), len(y))


def equil(x):
    '''利用相对挥发度算出y 来确定平衡线方程
       乙醇水体系的相对挥发度α=5.1016
    '''
    alpha = 5.1016
    yy = alpha * x / (1 + (alpha - 1) * x)
    return yy


# plt.plot(x,equil(x),linewidth=1.0,c='m',marker="^")#zorder=2
def runplt(size=None):
    plt.figure(figsize=(8, 8))
    plt.title(r'The Composition diagram of Ethanol(Full reflux)')
    plt.ylabel(r'$y$', fontsize=15)
    plt.xlabel(r'$x$', fontsize=15)
    plt.axis([0, 1, 0, 1])
    # plt.axis([])
    tick_params(direction='in')
    tick_params(top='on', bottom='on', left='on', right='on')
    return plt


def qm(x):
    '''将质量qulity分数转化为摩尔mol分数
       乙醇的分子量为46
       溶剂为水18
    '''
    M = 46

    return (x / M) / (x / M + (1 - x) / 18)


# def x_next(yp):
#     """采用从xw即自塔顶向塔底计算"""
#     x = sp.Symbol('x')
#     # x = sp.Symbol('x',real='True') # If only real number roots are required
#     f_X =631.4 *x**9 - 3012 *x**8 + 6101* x**7 - 6850 x + 4672 x - 2000 x + 539.9 x
#           2
#  - 90.55 x + 9.443 x + 0.0117
#     root_List = sp.solve(f_X)


print(qm(0.80), qm(0.07), qm(0.04), qm(0.8))
xd = qm(0.90)
xw = qm(0.07)
print(matplotlib.matplotlib_fname())
runplt()
A = np.polyfit(x, y, 9)
B = np.poly1d(A)
Y=[]
X=[]
def y_next():
    xw = qm(0.07)

    c=49

    while xw<xd:
        c+=1
        if c%2==0:
            yy = xw
            Y.append(yy)
            X.append(xw)
        else:
            X.append(xw)
            yy=B(xw)
            Y.append(yy)
        xw = yy


    return X,Y


print(y_next())
# print(B)
plt.plot(np.arange(0, 1, 0.001), B(np.arange(0, 1, 0.001)), ls='-', linewidth=1.0, c='black',
         label=r'Balanced relationship', zorder=2, )
plt.plot(np.arange(0, 1, 0.001), np.arange(0, 1, 0.001), ls='-', linewidth=1.0, c='dimgrey',
         label=r'Distillation section operation line')
plt.plot(x, y, linewidth=1.0, c='b', marker="*")  # zorder=2
# plt.plot(x, equil(x), linewidth=1.0, c='m', marker="^")
plt.plot(X, Y, linewidth=1.0, c='g', marker="<")
plt.legend(loc='upper left')
# 画点的注释
plt.annotate('W点', xy=(xw ,xw), xytext=(xw + 0.06, xw), arrowprops=dict(arrowstyle='->'))  # 画点的注释
plt.annotate('D点', xy=(xd, xd), xytext=(xd, xd - 0.06), arrowprops=dict(arrowstyle='->'))
# plt.annotate('(xe,ye)点', xy=(0.5, 0.658), xytext=(0.5,0.658 - 0.06), arrowprops=dict(arrowstyle='->'))
plt.savefig('../全回流.png'20, bbox_inches='tight')
plt.show()

