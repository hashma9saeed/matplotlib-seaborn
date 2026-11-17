import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("tips")

#Distribution data plots : to visualize the distribution of quantitative data
#1) histplot() / distplot():
sns.histplot(df["total_bill"],bins = 20,kde = True)
plt.show()
#displaying histplot for "total_bill" and "tip"
plt.subplot(1,2,1)
sns.histplot(df["total_bill"],bins = 20,kde = True)
plt.subplot(1,2,2)
sns.histplot(df["tip"],bins = 20,kde = True)
plt.show()

#2) jointplot() :
sns.jointplot(x = "total_bill" , y = "tip" , data  = df , kind  = "scatter")    
plt.show()

#3) pairplot() :
sns.pairplot(df , hue = "sex")
plt.show()

#4) rugplot() :
sns.rugplot(df)
plt.show()

#_____________________________________________________________________________________________________
#categorical data plots : to visualize the distribution of qualitative data

#1) countplot() :
sns.countplot(x = df["sex"] , hue = df["smoker"])
plt.show()

#2) barplot() :
#x_axis__ categorical data
#y_axis__quantitative data
sns.barplot(x = df["sex"] , y = df["total_bill"] , estimator = np.max)        #estimator by default is np.mean
plt.show()

#3) boxplot() : 
#x_axis__ categorical data
#y_axis__quantitative data
sns.boxplot(x = "tip" , y = "day" , data = df)
plt.show()

#4) stripplot() :
sns.stripplot(x = "sex" , y = "tip" , data = df)
plt.show()

#5) swarmplot() : 
sns.swarmplot(x = "sex" , y = "tip" , data = df)
plt.show()

#6) violinplot() :
sns.violinplot(x = "sex" , y = "tip" , data = df)
plt.show()

#combining both swarm and violin plot: both are bit similar
sns.swarmplot(x = "sex" , y = "tip" , data = df)
sns.violinplot(x = "sex" , y = "tip" , data = df)
plt.show()

#__________________________________________________________________________________________________________
#matrixplot() : ____works for numeric values

flights= sns.load_dataset("flights")
print(flights)

tips = sns.load_dataset("tips")
print("tips")

#1) heatmap() : represents correlation
tips_correlation = tips[["total_bill" , "tip" , "size"]]
print(tips_correlation.corr())
sns.heatmap(tips_correlation.corr(),annot = True)
plt.show()

#2) pivot heatmap() :
pi_flight = flights.pivot_table(values = "passengers",index = "month",columns = "year")
print(pi_flight)
sns.heatmap(pi_flight)
plt.show()

#3) regession plot() :
sns.lmplot(x = "total_bill" , y = "tip" , data = tips , hue = "sex")
plt.show()

#______________________________________________________________________________________________________