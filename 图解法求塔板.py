import numpy as np
import pandas as pd
import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# mpl.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.weight'] = 'bold'  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.size'] = 26  # 设置matplotlib整体用Times New Roman
# 设计型计算，需要5个参数parameter = (xF,xD,xW,R,q)
parameter = [0.5, 0.97, 0.04, 2, 1]
alpha = 2.5
qF = 100
xF, xD, xW, R, q = parameter


# 补充部分，求R_min 饱和蒸汽进料
# R_min = 1 / (alpha - 1) * (alpha * xD / xF - (1 - xD) / 1 - xF) - 1
# R = R_min * 1.5
# parameter = [xF, xD, xW, R, q]
# print('R:{}'.format(R))


# q线方程
def yq(x):
    if q==1:
        y = 0
    else:
        y = q / (q - 1) * x - 1 / (q - 1) * xF
    return y


# 平衡线方程
def yp(x):
    y = alpha * x / (1 + (alpha - 1) * x)
    return y


def xp(y):
    x = y / (alpha - (alpha - 1) * y)
    return x


# 精馏段操作方程
def yj(x):
    y = R / (R + 1) * x + xD / (R + 1)
    return y


# 提馏段操作方程
#   需要先求解qD和qW,为此，使用sympy求解
A = sympy.Matrix([[1, 1], [xD, xW]])
b = sympy.Matrix([qF, xF * qF])
qD, qW = A.solve(b)
qL = R * qD


#   提馏段操作方程
def yt(x):
    y = (qL + q * qF) / (qL + q * qF - qW) * x - qW / (qL + q * qF - qW) * xW
    return y


# 准备数据，q线，平衡线，精馏操作线，提馏操作线
x = np.linspace(0, 1, 50)
yq1 = yq(x)
yp1 = yp(x)
yj1 = yj(x)
yt1 = yt(x)

# 确定Q点
xq = ((R + 1) * xF + (q - 1) * xD) / (R + q)
yq = (xF * R + q * xD) / (R + q)
print(xq,yq)
# 逐板计算，求解每个塔板的平衡情况
yn = [xD]
xn = []

while xp(yn[-1]) > xW:
    xn.append(xp(yn[-1]))
    if xn[-1] > xq:
        yn.append(yj(xn[-1]))
    else:
        yn.append(yt(xn[-1]))
else:
    xn.append(xp(yn[-1]))
    print('N_T = {}'.format(len(xn)))

# 输出塔板上的平衡点，经过四舍五入的结果
yn_r = [round(i, 3) for i in yn]
xn_r = [round(i, 3) for i in xn]

print('塔板上的平衡点，经过四舍五入的结果:')
print('yn_r={}'.format(yn_r))
print('xn_r={}'.format(xn_r))

# 图解法计算理论塔板数的图示数据
xnt = [xD]
ynt = [xD]
for n, i in enumerate(xn):
    xnt.append(i)
    ynt.append(yn[n])
    xnt.append(i)
    if i >= xq:
        ynt.append(yj(i))
    else:
        ynt.append(yt(i))
# 画图
#   基础设置
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
print(x)

#   画图
ax.plot(x, x, ls='-', label='对角线')  # 画线

xq=[0.5,0.5]
yq=[0.5,0.7]



ax.plot(xq, yq, label='q线')
ax.plot(x, yp1, label='平衡线')
ax.plot(x, yj1, label='精馏操作线')
ax.plot(x, yt1, label='提馏操作线')
ax.plot(xn, yn, label='塔板操作平衡点', ls=':', marker='+', markersize=10)
ax.plot(xnt, ynt, label='图解法—理论塔板', ls=':')

ax.plot(xD, xD, marker='.', markersize=10)  # 画点
ax.plot(xW, xW, marker='.', markersize=10)
ax.plot(xq, yq, marker='.', markersize=10)

ax.annotate('W点', xy=(xW, xW), xytext=(xW + 0.06, xW), arrowprops=dict(arrowstyle='->'))  # 画点的注释
ax.annotate('D点', xy=(xD, xD), xytext=(xD, xD - 0.06), arrowprops=dict(arrowstyle='->'))
ax.annotate('(xe,ye)点', xy=(0.5, 0.658), xytext=(0.5,0.658 - 0.06), arrowprops=dict(arrowstyle='->'))
ax.legend()
#===坐标轴加粗==
ax=plt.gca();#获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);###设置右边坐标轴的粗细
ax.grid()
ax.text(x=0.6,y=0.4,s="所需理论板：%d"%(len(xn_r)-1))
ax.set_title("图解法求理论塔板数")
ax.set_ylabel("Y")
ax.set_xlabel("X")
plt.show()
fig.savefig('逐板计算法求理论塔板数.png',dpi=100,facecolor='#ffffff')
