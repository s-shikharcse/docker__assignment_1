import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
data1=pd.read_csv("C:\\Users\Sachin Jain\Desktop\dcker_test\Ex03_SystolicBP_Regreesion.csv")
from sklearn.model_selection import train_test_split
X=data1.iloc[:,0:-1]
Y=data1.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=4)