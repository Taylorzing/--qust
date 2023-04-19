from matplotlib.pyplot import plot, show, xlabel
from numpy import linspace
from sympy import symbols, exp, diff, log, E
x=[0.0145,0.3090,0.6765]
t=symbols("t")
#标准单位P:Kpa 摄氏度t:C
lgP=[6.05543-1115.5/(t+231),6.09036-1296.4/(t+221),6.09036-1296.4/(t+221)]
P=101.13
K=[]
for i in range(3):
    K.append(pow(10,lgP[i])/P)
print(K)
F=0
for i in range(3):
    f=K[i] * x[i]
    F += f
def xqf(f: float, a: int = 0, b: int = 200, epsilion: float = 1 / 10 ** 10, iter: int = 300) -> float:
    global x_1
    xa, xb = a, b
    for i in range(iter):
        fa = f.subs(t, xa)
        fb=f.subs(t, xb)
        # fb = f.evalf(f.subs(t, xb))
        x_1 = xb - (fb * (xb - xa) / (fb - fa))
        print("第", i + 1, "次迭代 ", "xa=", xa, "  x_1=", x_1, "  |xa - xb|=", abs(xa - xb))
        if abs(xb - xa) < epsilion:
                break
        else:
            xa, xb = xb, x_1
    return x_1
def dawfunc():
    yy=[]
    tt=linspace(0,200)
    for i in tt:
        yy.append(F.subs(t,i))
    xlabel("t/C")
    plot(tt,yy)
    plot([0,200],[1,1])
    show()
xqf(F-1)
dawfunc()





