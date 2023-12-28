import pandas as pd
# df=pd.read_csv('titanic_dataset.csv')
# print(df)
# print(df["Age"])
# ages=pd.Series([22,25,33],name="Age")
# print(ages)
# print(df["Age"].max())
# print(ages.max())
# aages = df[(df['Age'] > 20) & (df['Age']<30) & (df['Sex']=='female')]
# print(aages)
# passclasss=df[df['Pclass']==1]
# print(passclasss)
# passclasss=df[df['Pclass']==2]
# print(passclasss)
# passclasss=df[df['Pclass']==3]
# print(passclasss)
import matplotlib.pyplot as plt
import numpy as np
f=pd.read_csv('titanic.csv')
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# surived_count =f['Survived'].value_counts()
# plt.hist(f['Age'].dropna(),bins=20,edgecolor='black')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()
# plt.scatter(f['Age'],f['Fare'],alpha=0.5)
# plt.title('Fare vs Age')
# plt.xlabel('Age')
# plt.ylabel('Fare')
# plt.show()
# class_survival_counts=f.groupby('Pclass')['Survived'].value_counts().unstack()
# class_survival_counts.plot(kind='bar',stacked=True,color=['red','green'])
# plt.title('Survival Count by Passenger class')
# plt.xlabel('Passenger Class')
# plt.ylabel('Count')
# plt.legend(['Not Survived','Survived'],loc='upper right')
# plt.show()
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
v1=vector(1,2)
v2=vector(3,4)
result=v1+v2
print(result.x,result.y)       
