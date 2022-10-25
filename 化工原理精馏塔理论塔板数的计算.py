# 基本参数输入
parameter1 = []
F, W, D = parameter1
parameter2 = []
xf, xw, xd = parameter2
parameter3 = []
q, a, R = parameter3
# 基本方程的计算
yw = (a * xw) / (1 + (a - 1) * xw)
Rmin = (xd - yw) / (yw - xw)
print("最小回流比", Rmin)
if R == 0:
    k = eval(input("最小回流比倍数"))
    R = Rmin * k
    print("回流比", R)
yq = (R * xf + q * xd) / (R + q)
xq = ((R + 1) * xf + (q - 1) * xd) / (R + q)

# 基本方程的输出
print("平衡线方程：", "y=", a, "x/(1+", a, "-1)x")
if q != 1:
    print("q线方程：", "yq=", q / (q - 1), "xq-", xf / (q - 1))
else:
    print("yq=1")
print("精馏段方程：", "yn+1=", R / (R + 1), "xn+", xd / (R + 1))
print("提馏段方程：", "yn+1=", (R * D + q * F) / ((R + 1) * D - (1 - q) * F), "xn+",
      (D * xd - F * xf) / ((R + 1) * D - (1 - q) * F))

# 逐板计算
n = 0
y = xd
while True:
    x = y / (a - y * (a - 1))
    print(x)
    if x < xq:
        y = ((R * D + q * F) / ((R + 1) * D - (1 - q) * F)) * x + (D * xd - F * xf) / ((R + 1) * D - (1 - q) * F)
        print(y)
        n = n + 1
        print("提馏段", n)
        if x < xw:
            break
    else:
        y = (R / (R + 1)) * x + (xd / (R + 1))
        print(y)
        n = n + 1
        print("精馏段", n)
        j = n
print("提馏段理论塔板数：", j)
print("精馏段理论塔板数：", n - j)
print("全塔理论塔板数：", n)
