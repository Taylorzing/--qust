from matplotlib.pyplot import plot, show
from numpy import linspace
from sympy import symbols, exp, diff, log

from util2 import Newton

z = [0.4, 0.3, 0.3]
a = [9.0580, 9.2131, 9.2164]
b = [2154.90, 2477.07, 2697.55]
c = [-34.42, -39.94, -48.8]
P, T = 10.13, 122+273.15  # 1.013*10**3pa   122+273.15K
K = []
sum=-1
t = symbols("t")
for i in range(3):
    K.append(exp(a[i] - (b[i] / (c[i] + t)))/P)#安托因方程求相平衡常数
    # K.append(exp(a[i]+b[i]/t+c[i]*log(P)))#相平衡常数经验式
    # print(K,)
for i in range(3):
    f=(K[i] * z[i])
    sum += f
print("接近于1为正常:",abs(sum.subs(t,200)))
F=sum
print(F,P,T)
yy=[]
tt=linspace(0,200)
for i in tt:
    yy.append(sum.subs(t,i))
# yy=sum.subs(t,tt)
# print(tt)
print(yy)
plot(tt,yy,"*")
show()
# ffdx = diff(f, t, 2)#二阶导数
# print("二阶导数:",ffdx)
def Newton(f,x0=200, epsilon=1/10**4, iternum=100000000):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    fdx = diff(f, t)
    for i in range(iternum):
        fx=f.subs(t,xk_1)
        fdx=fdx.subs(t,xk_1)
        # ffdx=ffdx.subs(t,xk_1)
        if fdx != 0:
            xk = xk_1 - fx / fdx
            # xk=xk_1-2/((2*fdx)/fx-(2*ffdx/fdx))#Richmond
            print("第", i + 1, "次迭代 ", "xk=", xk, "  xk-1=", xk_1, "  |xk - xk-1|=", abs(xk - xk_1),"下降f/df：",fx/fdx);
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            break
    print("方法失败")
    return 0
# Newton(F,x0=20)

