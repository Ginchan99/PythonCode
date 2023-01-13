#import the packages
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
#%%
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
diab = pd.read_csv('Datasets/pima-indians-diabetes.csv',header=None,names=col_names)
#%%
diab.head()
#%%
x_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
y_cols = ['label']

#%%
XVals = diab[x_cols]
#%%
XVals.head()
#%%
YVals = diab[y_cols]

#%%
YVals.head()

#%%
randomSeed=7
#creating train and test datasets
XVals_train, XVals_test, YVals_train, YVals_test = train_test_split(XVals,YVals,test_size=0.25,random_state=randomSeed)
#%%
#initialize log reg model
lr = LogisticRegression(random_state=randomSeed)

#%%
lr.fit(XVals_train,YVals_train)
#%%
YPred=lr.predict(XVals_test)

#%%
#Creating a confusion matrix
from sklearn.metrics import confusion_matrix
#%%
conf_matrix = confusion_matrix(YVals_test,YPred)
#%%
#%%

#%%
class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

#%%
from sklearn.metrics import classification_report
clf = classification_report(YVals_test,YPred,target_names=['without diabetes','with diabetes'])
print("Classification report = ",clf)
#%%
#ROC Curve
YPred_variations = lr.predict_proba(XVals_test)
from sklearn.metrics import roc_curve

#%%
YPred_variations = YPred_variations[::,1]#only first col
fpr,tpr,other = roc_curve(YVals_test,YPred_variations)

#%%
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(YVals_test,YPred_variations)
#plot the results
plt.plot(fpr,tpr,label="auc="+str(round(auc,2)))
plt.legend(loc=4)
plt.show()

#%%
