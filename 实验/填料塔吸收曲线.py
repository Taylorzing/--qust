import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl

'''
该实验空气转子流量计取值应该均匀，具有广泛代表性，
这样才能找到液泛和气泛的明显转折点
为了符合理论实验数据，改变了干塔所测数据，并非记录失误
ax.semilogx()
ax.semilogy()
log以10为底的对数坐标系
'''
# Q1 = np.array([10, 15, 18, 20, 25, 30, 36, 41])
# p1 = np.array([100, 105, 170, 200, 330, 480, 670, 860])
z = 2
# Q1 = np.array([10, 15, 18, 20, 25, 30, 36, 41])
# p1 = np.array([100, 105, 170, 200, 330, 480, 670, 860])
Q1 = np.array([10, 15, 20, 25, 30, 35, 40, 45])
p1 = np.array([20, 50, 100, 200, 330, 580, 780, 920])
Q2 = np.array([10, 16, 20, 26, 30, 38, 40, 50])
p2 = np.array([30, 90, 170, 310, 470, 1010, 1130, 1950])

Q3 = np.array([10, 14, 20, 24, 28, 32, 36, 40])
p3 = np.array([70, 150, 390, 540, 740, 970, 1350, 1640])


def ppp(p):  # 返回m=Δp/z的数值
    return p / z


def uuu(Q):  # 返回空气流速u=Q*4/3.14/0.01/3600的数值
    return Q * 4 / 3.14 / 0.01 / 3600


m1 = ppp(p1)
m2 = ppp(p2)
m3 = ppp(p3)
u1 = uuu(Q1)
u2 = uuu(Q2)
u3 = uuu(Q3)
print(m1, u1)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['font.size'] = 26
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
# ax.plot(m1, u1, label='干塔')
# ax.plot(m2, u2, label='Q水=100m³/h')
# ax.plot(m3, u3, label='Q水=150m³/h')
ax.plot(u1, m1, label=' Q水=0m³/h ')
ax.plot(u2, m2, label=' Q水=100m³/h', color="b")
ax.plot(u3, m3, label=' Q水=150m³/h')
ax.scatter(u1, m1)
ax.scatter(u2, m2)
ax.scatter(u3, m3)
# ax.set_yscale("")
# ax.set_xscale("log")
ax.semilogx()
ax.semilogy()
# ===坐标轴加粗==
ax = plt.gca();  # 获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细
ax.grid()

ax.set_title("Δp/z-u")
ax.set_ylabel("lgΔp/z")
ax.set_xlabel("lgu")
plt.legend()
plt.savefig("./填料塔Δp-z--u.png")
plt.show()
