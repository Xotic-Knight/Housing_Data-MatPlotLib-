from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#create an error list
def error(l):
    w=[]
    for i in l:
        w.append(i**2)
    return w
#Function For calculating mean
def mean_number(l):
    sum=0
    for i in l:
        sum+=i
    return (sum/l.__len__())
#read csv
df=pd.read_csv('Housing.csv')
x=df['lotsize']
y=df['price']
#calculate mean
mean_x=mean_number(x)
mean_y=mean_number(y)
err_list_x=[]
for i in x:
    err_list_x.append(i-mean_x)#calculate(xi-x_mean)
err_list_y=[]
for i in y:
    err_list_y.append(i-mean_y)#calculate(yi-y_mean)
err_list_xy=[]
sumxy=0
for i in range(err_list_x.__len__()):
    err_list_xy.append(err_list_x[i]*err_list_y[i])#calculate product
for i in err_list_xy:
    sumxy+=i#sum of the product
sumx2=0
for i in err_list_x:
    sumx2+=i**2
#slope
slope=sumxy/sumx2
#constant
c=mean_y-slope*mean_x
yline=[]
for i in x:
    yline.append(slope*i+c)
plt.plot(x,yline,color='r')
sse=0
#sum of squared errors
for i in range(x.__len__()):
    sse+=(y[i] - (slope*x[i]+c))**2
print(sse)
err_list=[]
for i in y:
    err_list.append(i-mean_y)
e=error(err_list)
#sum of squared total
sst=0
for i in e:
    sst+=i
print(sst)
print(sse)
#sum of squared regression
ssr = sst-sse
print((ssr/sst)*100)
y1=slope*5000+c
plt.scatter([5000],y1,color='k',label='Point')
plt.scatter(x,y)
plt.show()