# -*- coding: utf-8 -*-
"""Assignment_7 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18w8uUIKAx071ZG6p4zsF0qMGKmLfACF2
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
 
# reading given tsv file
with open("Ratings.tsv", 'r') as myfile: 
  with open("Ratings.csv", 'w') as csv_file:
    for line in myfile:
       
      # Replace every tab with comma
      fileContent = re.sub("\t", ",", line)
       
      # Writing into csv file
      csv_file.write(fileContent)

# Importing CSV file into DataFrame using Pandas
df = pd.read_csv("/content/Ratings.csv")

df.info()

df.describe()

X = df[['restaurant', 'food', 'ambience', 'service']].to_numpy()
X

y = df['rating'].to_numpy()

"""# Gradient Descent"""

class MyLReg(object):
 
   def __init__(self, activation_function):
        self.activation_function = activation_function

   def fit(self, X, y, Learning_rate = 0.001, epochs = 100):
        self.theta = np.random.randn(X.shape[1] + 1)
        self.errors = []
        n = X.shape[0]
        self.m1,self.m2,self.m3,self.m4 = [],[],[],[] 
        i = 1
        for _ in range(epochs):
            Learning_rate = Learning_rate/i 
            errors = 0
            sum_1 = 0
            sum_2 = 0
            for xi, yi in zip(X, y):
                sum_1 += (self.predict(xi) - yi)*xi
                sum_2 += (self.predict(xi) - yi)
                errors += ((self.predict(xi) - yi)**2)
            self.theta[:-1] -= 2*Learning_rate*sum_1/n
            self.theta[-1] -= 2*Learning_rate*sum_2/n
            self.errors.append(errors/n)
            self.m1.append(self.theta[0])
            self.m2.append(self.theta[1])
            self.m3.append(self.theta[2])
            self.m4.append(self.theta[3])
            i = i+1
        print(self.theta)    
        return self

   def predict(self, X):
        weighted_sum = np.dot(X, self.theta[:-1]) + self.theta[-1]
        return self.activation_function(weighted_sum)

def identity_function(z):
    return z

model = MyLReg(identity_function)
model.fit(X, y, Learning_rate = 0.001, epochs = 100)
plt.plot(range(1, len(model.errors) + 1),(model.errors),marker = "*")
plt.xlabel("epochs")
plt.ylabel("MSE error")
plt.show()

plt.figure(figsize = (6,6))
plt.title('Gradient Descent')
plt.plot(range(100),model.m1, label='restaurant')
plt.plot(range(100),model.m2, label='food')
plt.plot(range(100),model.m3, label='ambience')
plt.plot(range(100),model.m4, label='service')
plt.legend()
plt.xlabel("epochs", fontsize = 8)
plt.ylabel("Parameters", fontsize = 8)
plt.show()

"""# stochastic gradient descent """

class MyLRegSGD(object):
    def __init__(self, activation_function):
        self.activation_function = activation_function

    def fit(self, X, y, alpha = 0.001, epochs = 100, batch_size = 32):
        self.theta = np.random.randn(X.shape[1] + 1)
        self.errors = []
        n = X.shape[0]
        self.m1,self.m2,self.m3,self.m4 = [],[],[],[] 
        a=1
        for i in range(epochs):
            errors = 0
            sum_1 = 0
            sum_2 = 0
            count = 0
            alpha= alpha/a 
            for xi, yi in zip(X, y):
                sum_1 += (self.predict(xi) - yi)*xi
                sum_2 += (self.predict(xi) - yi)
                errors += ((self.predict(xi) - yi)**2)
                    
                if count == batch_size-1:
                    self.theta[:-1] -= 2 * alpha * sum_1 / batch_size
                    self.theta[-1] -= 2 * alpha * sum_2 / batch_size
                    sum_1 = 0
                    sum_2 = 0
                    count = 0
                count += 1 
            if n%batch_size != 0:
                self.theta[:-1] -= 2 * alpha * sum_1 / (n % batch_size)
                self.theta[-1] -= 2 * alpha * sum_2 / (n % batch_size)
            temp = errors/n
            self.errors.append(temp)
            self.m1.append(self.theta[0])
            self.m2.append(self.theta[1])
            self.m3.append(self.theta[2])
            self.m4.append(self.theta[3])
            a=a+1
        return self


    def predict(self, X):
        weighted_sum = np.dot(X, self.theta[:-1]) + self.theta[-1]
        return self.activation_function(weighted_sum)

model1 = MyLRegSGD(identity_function)
model1.fit(X, y, alpha = 0.001, epochs = 100,batch_size= 32)
plt.plot(range(1, len(model1.errors) + 1),(model1.errors),marker = "*")
plt.xlabel("epochs")
plt.ylabel("MSE error")

plt.show()

plt.figure(figsize = (6,6))
plt.title('SGD parameters')
plt.plot(range(100),model1.m1, label='resturant')
plt.plot(range(100),model1.m2, label='food')
plt.plot(range(100),model1.m3, label='ambience')
plt.plot(range(100),model1.m4, label='service')
plt.legend()
plt.xlabel("epochs", fontsize = 8)
plt.ylabel("parameters", fontsize = 8)
plt.show()

"""Bonus Question"""

class MySGDReg(object):
    def __init__(self, activation_function):
        self.activation_function = activation_function

    def fit(self, X, y, Learning_rate = 0.001, epochs = 1000, batch_size = 32):
        self.theta = np.random.rand(X.shape[1] + 1)
        self.errors = []
        n = X.shape[0]
        self.m1,self.m2,self.m3,self.m4 = [],[],[],[]
        a = 1
        for i in range(epochs):
            errors = 0
            sum_1 = 0
            sum_2 = 0
            count = 0
            Learning_rate = Learning_rate/a 
            for xi, yi in zip(X, y):
                sum_1 += (self.predict(xi) - yi)*xi
                sum_2 += (self.predict(xi) - yi)
                errors += ((self.predict(xi) - yi)**2)
                if count == batch_size-1:
                    self.theta[:-1] -= 2 * Learning_rate * sum_1 / batch_size
                    self.theta[-1] -= 2 * Learning_rate * sum_2 / batch_size
                    sum_1 = 0
                    sum_2 = 0
                    count = 0
                count += 1 
            
            if n%batch_size != 0:
                self.theta[:-1] -= 2 *Learning_rate * sum_1 / (n % batch_size)
                self.theta[-1] -= 2 * Learning_rate * sum_2 / (n % batch_size)
            temp = errors/n
                  
            self.errors.append(temp)
            self.m1.append(self.theta[0])
            self.m2.append(self.theta[1])
            self.m3.append(self.theta[2])
            self.m4.append(self.theta[3])
            a = a+1
            self.errors.append(temp)
        return self


    def predict(self, X):
        weighted_sum = np.dot(X, self.theta[:-1]) + self.theta[-1]
        return self.activation_function(weighted_sum)

def identity_function(z):
    return z

model2 = MySGDReg(identity_function)
model2.fit(X, y, Learning_rate = 0.001, epochs = 1000,batch_size= 32)
plt.plot(range(1, len(model2.errors) + 1),(model2.errors),marker = "*")
plt.xlabel("epochs")
plt.ylabel("MSE error")

plt.show()

print('mean of model2.resturant=', np.mean(model2.m1))
print('mean of model2.food =', np.mean(model2.m2))
print('mean of model2.ambience=', np.mean(model2.m3))
print('mean of model2.service=', np.mean(model2.m4))

import statsmodels.formula.api as sm
reg= sm.ols('rating ~ food+ambience+service',data=df).fit()
reg.summary()

