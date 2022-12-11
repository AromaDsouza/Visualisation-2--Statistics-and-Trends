# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:09:06 2022

@author: Aroma
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def population(read_the_file):
    dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
    dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,40,50,60]]
    #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
    dataframe1 = dataframe1.dropna(axis=1)
    dataframe2 = dataframe1.T
    #print(dataframe1,dataframe2)
    return dataframe1, dataframe2
a,b = population("Population.csv")
print(a)
print(b)
a.plot(kind="bar", x = 'Country Name', rot=0, figsize= (10,10))
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
plt.title("Total Population",fontsize=25) #To mention the title for stacked bar graph
plt.legend(loc='upper right',fontsize=20)  #To show the label names in form of a box
plt.savefig('Side by side bar graph1.png') #Saving the image of the line graph
plt.show()  #To display the image of the line graph

def forest_area(read_the_file):
    dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
    dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,20,30,40,50,60]]
    #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
    dataframe1 = dataframe1.dropna(axis=1)
    dataframe2 = dataframe1.T
    #print(dataframe1,dataframe2)
    return dataframe1, dataframe2
c,d = forest_area("Forest Area in sq km.csv")
print(c)
print(d)
c.plot(kind="bar", x = 'Country Name', rot=0, figsize= (10,10))
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
plt.title("Forest Area (sq. km)",fontsize=25) #To mention the title for stacked bar graph
plt.legend(loc='upper right',fontsize=20)  #To show the label names in form of a box
plt.savefig('Side by side bar graph2.png') #Saving the image of the line graph
plt.show()  #To display the image of the line graph

def carbon_dioxide_emissions(read_the_file):
        dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
        dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,40,50,60]]
        #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
        dataframe1 = dataframe1.dropna(axis=1)
        dataframe2 = dataframe1.set_index('Country Name').T
        #rint(dataframe1,dataframe2)
        return dataframe1, dataframe2 
    
e,f = carbon_dioxide_emissions("CO2 Emissions.csv")
print(e)
print(f)
e["Average"] = np.mean(e, axis=1)
print(e)
print(f)

avg_data = e["Average"]
#explode = (0, 0, 0, 0.2, 0, 0.2, 0, 0.2)
plt.figure(dpi = 144, figsize = (10,10))
plt.pie(avg_data, labels = e['Country Name'], autopct = "%2.2f%%")
plt.axis('equal') 
plt.xlabel("Countries",fontsize=20)  #To label the x-axis
#plt.xticks(rotation=45)
plt.title("CO2 Emissions (kt) ", fontsize=20)  #To display the image of the pie graph
plt.legend(loc='best',fontsize=10)#To show the label names in form of a box
plt.savefig('Pie chart1.png') #Saving the image of the line graph
plt.show()

def renewable_energy(read_the_file):
        dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
        dataframe1 = dataframe1.iloc[[35,40,77,81,109,113,119,126],[0,40,50,60]]
        #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
        dataframe1 = dataframe1.dropna(axis=1)
        dataframe2 = dataframe1.set_index('Country Name').T
        #rint(dataframe1,dataframe2)
        return dataframe1, dataframe2 
    
m,n = renewable_energy("Renewable energy.csv")
print(m)
print(n)
m["Average"] = m.iloc[:, 1:5].mean(axis=1)
print(m)
print(n)

avg_data = m["Average"]
#explode = (0, 0, 0, 0.2, 0, 0.2, 0, 0.2)
plt.figure(dpi = 144, figsize = (10,10))
plt.pie(avg_data, labels = m['Country Name'], autopct = "%2.2f%%")
plt.axis('equal') 
plt.xlabel("Countries",fontsize=20)  #To label the x-axis
#plt.xticks(rotation=45)
plt.title("Renewable energy (%)", fontsize=20)  #To display the image of the pie graph
plt.legend(loc='best',fontsize=10)#To show the label names in form of a box
plt.savefig('Pie chart2.png') #Saving the image of the line graph
plt.show()
#print(y.describe())
#print(y)
def climate_change(read_the_file):
    dataframe1 = pd.read_csv(read_the_file, skiprows = 4) #first read the data,convert to dataframe
    dataframe1 = dataframe1.fillna(0)
    dataframe1 = dataframe1.loc[dataframe1['Country Name'] == 'India' ]
    indicator = ['Population, total','Forest area (sq. km)','CO2 emissions (kt)',
             'Renewable energy consumption (% of total final energy consumption)']
    filter = dataframe1['Indicator Name'].isin(indicator)
    dataframe2 = dataframe1.loc[filter]
    dataframe2 = dataframe2.drop(['Country Name','Country Code','Indicator Code'],axis=1)
    dataframe3 = dataframe2.set_index('Indicator Name').T
    print(dataframe3)
    return dataframe1, dataframe2, dataframe3
x,y,z = climate_change("Master_dataset.csv")
print(z)

correlation = z.corr(method='pearson')
correlation
#a = sns.heatmap(correlation , linewidth = 0.5 , cmap = 'coolwarm', annot=True)
sns.heatmap(correlation, 
            xticklabels=correlation.columns,
            yticklabels=correlation.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)