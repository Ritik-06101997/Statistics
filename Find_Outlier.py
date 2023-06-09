import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Define our dataset
data= [11,10,12,14,12,15,14,13,15,102,12,14,13,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,14,13,15,10]
plt.hist(data)

# Finding outlier using Z Score= (Xi-mean)/std
outliers=[]

def detect_outliers(data):
  threshold=3 # #rd std deviation
  mean= np.mean(data)
  std= np.std(data)

  for i in data:
    z_score= (i-mean)/std
    if np.abs(z_score) > threshold:
      outliers.append(i)
  return outliers
detect_outliers(data)

# IQR
"""
1.Sort the dataset
2.Calculate Q1 and Q3
3.IQR = Q3-Q1
4.Find the lower fence -> Q1- 1.5(IQR)
5. Find the upper fence -> Q3+ 1.5(IQR)
"""
dataset = sorted(data)
dataset
Q1,Q3 = np.percentile(dataset,[25,75])

print(Q1,Q3)

IQR= Q3-Q1
print(IQR)

Lower_fence= Q1 -(1.5* IQR)
Upper_fence= Q3 +(1.5* IQR)

print(Lower_fence,Upper_fence)

sns.boxplot(dataset)

