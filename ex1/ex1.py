import pandas as pd, numpy as np, matplotlib.pyplot as plt,os
#1. make an identity matrix
def warmUpExercise():
    return np.eye(5)
#2.1
def plotData(X,y):
    plt.plot(X.iloc[:,1],y,'x',label="Actual Data")
    plt.xlabel("Population of City in 10,000")
    plt.ylabel("Profit in $10,000")
    plt.xlim(4,24)
    plt.ylim(-5,25)
    plt.legend()
    plt.show()
#2.2
def computeCost(X,y,theta):
    X=np.array(X)
    y=np.array(y)
    theta=np.array(theta)
    m=len(y)
    J=(1/(2*m))*((sum((np.dot(X,theta)-y)**2)))
    return J
#2.2.4
def graddec(X,y,theta,alpha,num_iters):
    m=len(y)
    data=np.zeros(shape=[num_iters,1])
    for i in range(num_iters):
        theta=theta-(alpha*(1/m)*(np.dot((np.dot(X,theta)-y),X)))
        data[i][0]=computeCost(X,y,theta)
    return theta,data
#Loading Data
path=os.getcwd()+"\ex1data1.txt"
df=pd.read_csv(path,header=None)
X=pd.DataFrame(df.loc[:,0])
y=df.loc[:,1]
#2.2 
m=len(X)
X.insert(0,1,1)
theta =[0,0]
iterations = 1500;
alpha = 0.01;
theta,data=graddec(X,y,theta,alpha,iterations)
print("Theta computed from gradient descent is: ",theta[0],theta[1])
plt.plot(X.iloc[:,1],np.dot(X,theta),label="Linear reg")
plt.legend()
plt.show()