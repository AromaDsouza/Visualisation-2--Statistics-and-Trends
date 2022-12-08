# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:09:06 2022

@author: Aroma
"""
import pandas as pd
import matplotlib.pyplot as plt

def urban_population(read_the_file):
    dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
    #dataframe1 = dataframe1.iloc[[11:20],[0,40,50,60]]
    dataframe1 = dataframe1.filter(items=[35,40,77,81,109,113,119,126], axis=0)
    dataframe1 = dataframe1.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
    #dataframe1 = dataframe1.filter(items=['Country Name','2000','2001','2002','2003'], axis=1)
    dataframe1 = dataframe1.dropna(axis=1)
    dataframe2 = dataframe1.set_index('Country Name').T #dataframe2 = dataframe1.T #print(dataframe1,dataframe2
    return dataframe1, dataframe2    
a,b = urban_population("Urban population.csv")
print(a)
print(b)
b.plot(kind="line", rot= 0, figsize= (20,10))
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
#plt.xticks(rotation=45)
plt.title("Urban Population (%)",fontsize=25) #To mention the title for bar graph
plt.legend(loc='best',fontsize=20)  #To show the label names in form of a box
plt.savefig('Line graph1.png') #Saving the image of the line graph
plt.show()
'''
plt.figure(figsize=(20,10),dpi=144)
plt.plot(a['Country Name'],a["2000"],label="2000")
plt.plot(a['Country Name'],a["2001"],label="2001")
plt.plot(a['Country Name'],a["2002"],label="2002")
plt.plot(a['Country Name'],a["2003"],label="2003")

'''
def green_house_gases(read_the_file):
    dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
    dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,20,30,40,50,60]]
    #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
    dataframe1 = dataframe1.dropna(axis=1)
    dataframe2 = dataframe1.T
    #print(dataframe1,dataframe2)
    return dataframe1, dataframe2
c,d = green_house_gases("Greenhouse gases.csv")
print(c)
print(d)
c.plot(kind="bar", x = 'Country Name', rot=0, figsize= (10,10))
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
plt.title("Greenhouse gases (kt of CO2)",fontsize=25) #To mention the title for stacked bar graph
plt.legend(loc='upper right',fontsize=20)  #To show the label names in form of a box
plt.savefig('Side by side bar graph1.png') #Saving the image of the line graph
plt.show()  #To display the image of the line graph

def forest_area(read_the_file):
        dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
        dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,20,30,40,50,60]]
        #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
        dataframe1 = dataframe1.dropna(axis=1)
        dataframe2 = dataframe1.set_index('Country Name').T
        #rint(dataframe1,dataframe2)
        return dataframe1, dataframe2 

e,f = forest_area("Forest Area in sq km.csv")
print(e)
print(f)
e["Avg"] = e.iloc[:, 1:5].mean(axis=1)
print(e)
print(f)
e.plot(kind="pie",rot= 0, figsize= (20,10),y = 'Avg',labels = e['Country Name'])
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
#plt.xticks(rotation=45)
plt.title("Forest Area in sq km", fontsize=25)  #To display the image of the pie graph
#plt.legend(loc='upper right',fontsize=10)#To show the label names in form of a box
plt.savefig('Pie chart.png') #Saving the image of the line graph
plt.show()

def renewable_energy(read_the_file):
    dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
    #dataframe1 = dataframe1.iloc[[11:20],[0,40,50,60]]
    dataframe1 = dataframe1.filter(items=[35,40,77,81,109,113,119,126], axis=0)
    dataframe1 = dataframe1.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
    #dataframe1 = dataframe1.filter(items=['Country Name','2000','2001','2002','2003'], axis=1)
    dataframe1 = dataframe1.dropna(axis=1)
    dataframe2 = dataframe1.set_index('Country Name').T #dataframe2 = dataframe1.T #print(dataframe1,dataframe2
    return dataframe1, dataframe2    
g,h = renewable_energy("Renewable energy.csv")
print(g)
print(h)
h.plot(kind="line", rot= 0, figsize= (20,10))
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
#plt.xticks(rotation=45)
plt.title("Renewable Energy (%)",fontsize=25) #To mention the title for bar graph

plt.legend(loc='best',fontsize=20)  #To show the label names in form of a box
plt.savefig('Line graph2.png') #Saving the image of the line graph
plt.show()

'''
plt.figure(figsize=(20,10),dpi=144)
plt.plot(g['Country Name'],g["2000"],label="2000")
plt.plot(g['Country Name'],g["2001"],label="2001")
plt.plot(g['Country Name'],g["2002"],label="2002")
plt.plot(g['Country Name'],g["2003"],label="2003")
'''
