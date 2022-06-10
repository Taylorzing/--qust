import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

dp=[0.05,0.07,0.09]
A0=(0.131/2)**2*3.14*10
print("面积为A0:%f"%A0)
#时间加60s
dt1=np.array([71.82,67.26,74.71,82.45,85.69,79.78,85.19])#总共9:18.97
dt2=np.array([47.35,49.33,51.60,48.67,51.73,56.49,57.73]) #总共6:59.62  数据有噪声 第一个平均超10  倒数第二个超6
dt3=np.array([34.61,32.58,33.18,37.32,38.38,40.50,39.97]) #总共4:38.61

V=np.arange(0.8,6.0,0.8)  #体积每次0.8L
q=np.array(V/A0)
dq=(0.8/A0)
print(q,"\ndl/A为:",dq)
# df=pd.DataFrame(dt1,dt2,dt3,q)

X=q
def oneK(dtime,press,i=1):
    dtdq=dtime/dq
    Y1=dtdq
    print("dt/dq为:",Y1)

    # 一元线性回归
    slope,intercept,r_value,p_value,std_err=stats.linregress(X,Y1)

    print("%fMpa下的一元表达式为："%press)
    print("y=%fx+%f   "%(slope,intercept))
    print("K=%f,qe=%f"%(2/slope,intercept/slope))
    y=slope*X+intercept
    # plt.subplot(3,1,i)
    i=i+1
    plt.plot(X,y)
    plt.xlabel("q")
    plt.ylabel("dt/dl")
    plt.scatter(X,Y1)
    plt.title("dt/dq-q, Press={}MPa".format(press))
    plt.text(np.median(X),np.median(Y1),s=("y=%fx+%f\nK=%f,qe=%f\nθ=%f"
    %(slope,intercept,2/slope,intercept/slope,np.power(intercept/slope,2)/2*slope)))

    plt.grid()
    plt.legend()

oneK(dt1,0.05)
oneK(dt2,0.07)
oneK(dt3,0.09)
plt.show()