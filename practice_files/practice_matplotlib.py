import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#----------------------------   BASIC IMPLEMENTATION    ---------------------------------------------
x1 = [1,2,3,4,5]
x2 = [6,7,8,9,10]
plt.plot(x1,x2)
plt.title("basic implementation")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()

#-----------------------------   LINE PLOT  ------------------------------------------------------------

data = {
    "Salary" : [25000,4000,13000,20000,11000,55000,32000,5000,79000,56000,1000,13000,34000,56000,15000]
}
df = pd.DataFrame(data)
print(df.head())
print(df.shape)
plt.plot(df["Salary"], color = "purple" , marker = "*" , linestyle = "-" , linewidth = 1)
plt.title("Salary Line Plot")
plt.xlabel("index")
plt.ylabel("salary")
plt.show()

#--------------------------  PIE CHART  -------------------------------------------------------------

brands = ["oneplus","redmi","apple","nokia"]
price= [60000,5000,8000,2000]
ex =[0.1, 0, 0, 0] 
#0.1 ____ move the slice slightly outward
#1 ______ keep the slice in its normal position                                
plt.pie(price , labels = brands,shadow = True,explode=ex,autopct= "%.2f%%")
plt.show()

#---------------------------  HISTOGRAM   -------------------------------------------------------

Ages = [12,45,67,89,34,8,90,12,34,56,77,51,45]
plt.hist(Ages,bins = 5,color = "pink",edgecolor = "black")
plt.show()

#-----------------------------  BOX PLOT   -------------------------------------------------------

plt.boxplot(df["Salary"], orientation="vertical", showmeans=True, showfliers=True)
plt.show()


#----------------------------   BAR GRAPH    ---------------------------------------------------------

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones","USB Drive", "Printer", "Webcam", "Speakers", "Router","Tablet", "Smartphone", "Power Bank", "Microphone","External HardDrive"]
sales = [25, 40, 30, 18, 35, 50, 12, 22, 28, 15, 20, 45, 32, 10, 16]
plt.bar(products , sales , color = "red" , width = 0.6 , label = "Sales")
plt.show()

#---------------------------  SCATTER PLOT   -------------------------------------------------------

hours = [2, 4, 3, 5, 1, 6, 2, 3, 4, 5, 1, 7, 3, 2, 6]
marks = [75, 88, 65, 92, 55, 80, 70, 85, 60, 95, 50, 78, 89, 68, 83]
plt.scatter(hours , marks , color = "orange" , s = 100 , marker = "*" , alpha = 0.7)
plt.show()
 
# --------------------------  AREA PLOT  ------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 250]
plt.fill_between(months, sales, color="skyblue", alpha=0.5)
plt.plot(months, sales, color="blue", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#-----------------------------  SUB PLOT   -------------------------------------------------------
x = np.linspace(0,5,11)
print(x)
y = x**2
print(y)
plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.plot(x**3,y)
plt.subplot(2,2,4)
plt.show()
fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
axis1.plot(x,y)
axis2 = fig.add_axes([0.1,0.1,0.3,0.8])
axis2.plot(x,y)
plt.show()

#*******************************************************************************************************

#save the plot
fig = plt.figure()
axis = fig.add_axes([0.1,0.1,0.8,0.8])                 #fig.add_axes([left, bottom, width, height])
axis.plot(x,y)
plt.savefig("basicplot.png")

#working with images
import matplotlib.image as mpimg
img = mpimg.imread("image.jpeg")
plt.imshow(img)
plt.axis("off")