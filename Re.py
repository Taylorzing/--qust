import numpy as np
from matplotlib import pyplot as plt

Vs1 = np.array([1.63, 1.89, 2.25, 2.50, 2.97, 3.3, 3.4, 3.55, 4.6, 4.85, 5.15])
p1 = np.array([0.7, 1.8, 2.9, 5.0, 7.4, 9.2, 10.7, 12.6, 22.5, 26.2, 31.0])  # 单位为Kpa

R1 = np.array([140, 300, 500, 850, 1100, 1600, 2600, 3180, 4800, 5480, 6700])
R2 = np.array([350, 630, 1160, 1770, 2510, 3230, 4000, 4400, 4950, 5210, 5740])
Vs2 = np.array([0.7, 1, 1.4, 1.69, 2, 2.4, 2.8, 3.2, 4.30, 4.55, 5.05])
# print(len(Vs2), len(R1), len(R2))


# 计算管路面积A0
def A0(d):
    A = pow(d, 2) * np.pi
    return A


def U(vs, d):
    u = vs * 4 / A0(d) / 3600  # u单位为m/s   Vs为m^3/h
    return u


# print(U(vs=Vs2, d=0.025))
# print(U(vs=Vs2, d=0.02))


# Vs为体积流速  Re为雷诺数
def Re(vs, d=0.015128):
    re = d * 1000 * U(vs, d) / 1.0828 / 0.001
    return re


x = Re(vs=Vs1)


# C0为孔流系数  p为压差
def C0(vs, p, d=0.015128):
    c0 = (vs / A0(d) / 3600) * np.sqrt(1000 / (2 * p * 1000))
    return c0


# # print(A0(0.025))
y=C0(vs=Vs1, p=p1)
# print(y)
plt.plot(x,y,"r--*")
plt.xscale("log")

def yta1(u1, u2, r1):
    y = 2 / pow(u2, 2) * ((596 * 9.81 * r1 * 0.00000001) + (pow(u1, 2) - pow(u2, 2)) / 2)  # * 0.001
    return y


def yta2(u3, u4, r2):
    y = (2 / pow(u3, 2)) * ((-596 * 9.81 * r2 * 0.00000001) + ((pow(u3, 2) - pow(u4, 2)) / 2))  # * 0.001
    return y


print(yta1(U(vs=Vs2, d=0.025), U(vs=Vs2, d=0.02), r1=R1))
print(yta2(U(vs=Vs2, d=0.020), U(vs=Vs2, d=0.025), r2=R2))
# print(A0(0.0025), A0(0.002))
plt.show()
# q=(-596 * 9.81 * R2 * 0.000001)
# print(q)
# y=(pow(U(Vs2,0.025), 2) - pow(U(Vs2,0.02), 2)) / 2
# print(y)
