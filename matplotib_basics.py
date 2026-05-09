#matlotib is a python library used for data visulaization
import matplotlib.pyplot as plt
#pyplot is a collection of functions that make matplotlib works as MAT LAB

#create first chart 
# x=[1,2,3,4,5]
# y=[100,20,35,46,29]
# plt.plot(x,y)  #line chart
# plt.show()#display chart 


#customize chart 
# plt.figure(figsize=(10,10))  #figure size 
# plt.plot(x,y,  color="blue",marker="o" ,linestyle="dashed" , linewidth=2 , markersize=10)
# plt.title("Title of figure")
# plt.xlabel("values of x")
# plt.ylabel("values of y label")
# plt.show()


# #advance line chart
# x=[1,2,3,4,5]
# y1=[10000,2000,9999,19999,22323]
# y2=[100222,34999,44545,45444,44999]
# plt.plot(x,y1,label=" Salary 2024")  #plotting y1 data
# plt.plot(x,y2,label=" Salary 2025")  #plotting y2 data
# plt.title("Salary comparison")
# plt.xlabel("Months")
# plt.ylabel("Salary")
# plt.legend()
# plt.show()



#Bar chart
# x=[1,2,3,4,5]
# y=[10,20,30,40,50]
# plt.bar(x,y)
# plt.title("Bar chart example")
# plt.xlabel("x")
# plt.ylabel("Y")
# plt.show()



#Histogram: used for distribution 
# data=[11,22,34,45,32,77,99,56,58,79,45,66,43,78,79,70,12]
# plt.hist(data,bins=5)
# plt.title("Histogram")
# plt.show()


#pie chart: used to show the part
# marks=[91,86,90,82,82]
# sub=["Eng","Maths","Hindi","Physics","Chem"]

# plt.pie(marks,labels=sub,autopct="%1.1f%%" )
# plt.title("Marks distribution")
# plt.show()


#scatter plot : used to find relationship b/w variables
# x=[11,22,35,47,55]
# y=[10,20,30,40,50]

# plt.scatter(x,y)
# plt.title("Scatter plot")
# plt.show()


#subplots: used to show multiple chart in one figure

# #data1  -Bar chart 
# week=["Mon","Tue","Wed","Thu","Fri"]
# sales=[10,20,30,40,50]

# #data 2 -Scatter plot
# x=[11,22,35,47,55]
# y=[10,20,30,40,50]


# plt.figure(figsize=(6,4))

# #first plot-bar chart
# plt.subplot(1,2,1) #row ,column , position
# plt.bar(week,sales)
# plt.title("Daily Sales")
# plt.xlabel("Weeek_Days")
# plt.ylabel("Sales")

# #second plot - Scatter chart
# plt.subplot(1,2,2) #row ,column , position
# plt.scatter(x,y)
# plt.title("User example")
# plt.xlabel("x values")
# plt.ylabel("y values")

# plt.show()


#matplotib with pandas -real data
import pandas as pd

data={
    "Name": ["Garima","Ansh","Adarsh","Dibbi"],
    "Age": [19,20,21,23],
    "Salary": [90000,89000,50000,12000]


}
df=pd.DataFrame(data)
print(df)

plt.bar(df["Name"],df["Salary"])
plt.title("Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.show()

#save plots
plt.bar(df["Name"],df["Salary"])
plt.title("Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.savefig("Salary_compare.png")

plt.show()



