import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
'''注意单位换算'''

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['font.size'] = 26
fig, ax = plt.subplots(1, 1, figsize=(9, 9))

x = np.array([500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 1000, 1000])

t = np.array([52, 48, 47, 50, 46, 46, 49, 46, 50, 46, 129, 175])


def coef():  # 计算-Gc/S (g->Kg *0.001  平方零米->㎡ *0.01)
    return 110.8 * 0.001 / (7.4 * 5.4 + 5.4 * 1.4 + 7.4 * 1.4) / 2 / 0.01


def uu(x, t):
    return coef() * x * 0.000001 / t
print(coef())
print((7.4 * 5.4 + 5.4 * 1.4 + 7.4 * 1.4) * 2 * 0.01)
G = 118.8*0.001

u = uu(x, t)

X = []
x = x * 0.000001

# print(x)
for i in x:
    G -= i
    X.append(G)

ax.plot(X, u)#, label='--'
ax.scatter(X, u, marker='^')

ax = plt.gca();  # 获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细
ax.grid()

ax.set_title("u-X干燥速率曲线")
ax.set_ylabel("U/(kg/(㎡.h)")
ax.set_xlabel("X/(kg 水/kg 绝干料)")
plt.legend()

plt.savefig("./恒定干燥条件下干燥速率曲线.png")
plt.show()