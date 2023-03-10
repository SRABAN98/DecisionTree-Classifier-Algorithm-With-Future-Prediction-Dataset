#Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Import the dataset
dataset = pd.read_csv(r"C:\Users\dell\OneDrive\Documents\Data Science\3.Aug\9th,10th\5. DECESSION TREE CODE\Social_Network_Ads.csv")


#Splitting the dataset into I.V and D.V
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values


#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


#Feature Scalling does not required for the Tree algorithm, but we can cross check with that
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
'''


#Training the Decision Tree Classification model on the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion="gini", splitter="best", max_depth=5, min_samples_split=2, min_samples_leaf=1)
classifier.fit(X_train, y_train)


#Predicting the Test set results
y_pred = classifier.predict(X_test)


#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)


#Compute the accuracy score
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)


#Calculate the bias for the model
bias = classifier.score(X_train, y_train)
bias


#Calculate the variance for the model
variance = classifier.score(X_test, y_test)
variance


#Plot ROC Curve
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, linewidth=2)
plt.plot([0,1], [0,1], "k--" )
plt.rcParams["font.size"] = 12
plt.title("ROC curve for XUV purchased or not")
plt.xlabel("False Positive Rate (1 - Specificity)")
plt.ylabel("True Positive Rate (Sensitivity)")
plt.show()


#Compute ROC-AUC score
from sklearn.metrics import roc_auc_score
ROC_AUC = roc_auc_score(y_test, y_pred)
ROC_AUC



#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#


#------------------------FUTURE PREDICTION--------------------------


#import the future prediction dataset
dataset1 = pd.read_csv(r"C:\Users\dell\OneDrive\Documents\Data Science\3.Aug\3rd\Future prediction1.csv")


#copy the future prediction dataset in to a new variable
d2 = dataset1.copy()


#clean the future prediction dataset for the further operation
dataset1 = dataset1.iloc[:,[2, 3]].values


#Feature Scalling of the future prediction dataset does not required for the Tree algorithm
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
M = sc.fit_transform(dataset1)
'''


#creating the future prediction dataframe
y_pred_DTClassifier = pd.DataFrame()

d2["y_pred_DTClassifier"] = classifier.predict(dataset1)


#save the future prediction dataframe as the .csv file format
d2.to_csv("FPofDTClassifierAlgo.csv")


#To get the path where exactly the predicted .csv file saved in our desktop
import os
os.getcwd()
