from cv2 import norm
import pandas as pd, numpy as np, matplotlib.pyplot as plt,os
def setup():
    path=os.getcwd()+"\ex1"+"\ex1data2.txt"
    df=pd.read_csv(path,header=None)
    X=df.iloc[:,[0,1]]
    y=df.iloc[:,2]
    return X,y
X,y=setup()
m=len(y)
def average(x):
    return sum(x)/len(x)
def std(x):
    myu=average(x)
    x=np.array(x)
    x=x-myu
    std=sum(x**2)/len(x)
    return std
def normalize(x):
    sd=std(x)
    myu=average(x)
    x=np.array(x)
    x=(x-myu)/sd
    return x
X.iloc[:,0]=normalize(X.iloc[:,0])
print()
X.iloc[:,1]=normalize(X.iloc[:,1])
y=normalize(y)
X.insert(0,2,1)
