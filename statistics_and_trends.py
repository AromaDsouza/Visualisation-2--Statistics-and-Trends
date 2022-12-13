# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:09:06 2022

@author: Aroma
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def population(total_population_data):
    
    '''
    The above function named population produces a grouped bar graph i.e side 
    to side bar graph of the dataset from World Bank data.
    total_population_data: It is the dataset used for plotting the bar graph
    '''
    
    #To read the data and create a dataframe
    dataframe1 = pd.read_csv(total_population_data, skiprows=4)  
    #To select the desired rows and columns respectively
    dataframe1 = dataframe1.iloc[[35, 40, 77, 81, 109, 113, 119, 126],
                                 [0, 40, 50, 60]]
    #To drop the NaN or empty cells in the columns
    dataframe1 = dataframe1.dropna(axis=1)  
    dataframe2 = dataframe1.T  #Taking the transpose of the dataframe1
    return dataframe1, dataframe2
#Calling the function to read the population dataset
a,b = population("Population.csv")
#Printing the variables a and b assigned to the function
print(a)  #As a = dataframe1  
print(b)  #and b = dataframe2

'''
First visualisation: Grouped bar graph
Plotting the bar graph using pandas library by taking Country Name in the X axis 
and the years for the Y axis using the total population dataset.
'''

#Rot=0 keeps the country name straight without any rotation on the X axis
a.plot(kind="bar", x = 'Country Name', rot=10, figsize=(8, 6), edgecolor='black')

plt.xlabel("Countries",fontsize=15)  #To label the x-axis
plt.title("Total Population", fontsize=20) #To mention the title for bar graph
#Legend shows the label names in form of a box on the upper right hand of the image
plt.legend(loc='upper right', fontsize=15)
#Saving the image of the bar graph and dpi is dots per inch
#i.e to set the resolution of the image and to produce a clear image.
plt.savefig('Side by side bar graph1.png', dpi = 144) 
plt.show()  #To display the image of the bar graph

def forest_area(forest_area_data):
    
    '''
    The above function named forest_area produces a grouped bar graph 
    i.e side to side bar graph of the dataset from World Bank data
    forest_area_data: It is the dataset used for plotting the bar graph
    '''
    
    #To read the data and create a dataframe
    dataframe1 = pd.read_csv(forest_area_data, skiprows=4)
    #To select the desired rows and columns respectively
    dataframe1 = dataframe1.iloc[[35, 40, 77, 81, 109, 113, 119, 126],
                                 [0, 20, 30, 40, 50, 60]]
    #To drop the NaN or empty cells in the columns
    dataframe1 = dataframe1.dropna(axis=1)  
    dataframe2 = dataframe1.T  #Taking the transpose of the dataframe1
    return dataframe1, dataframe2
#Calling the function to read the forest area dataset
c,d = forest_area("Forest Area in sq km.csv")
#Printing the variables c and d assigned to the function
print(c)  #as c = dataframe1 
print(d)  #and d = dataframe2

'''
Second visualisation: Grouped bar graph
Plotting the bar graph using pandas library by taking Country Name in the X axis 
and the years for the Y axis using the forest area dataset.
'''

#Rot=0 keeps the country name straight without any rotation on the X axis
c.plot(kind="bar", x = 'Country Name',rot=10, figsize=(8, 6), edgecolor='black')  
plt.xlabel("Countries", fontsize=15)  #To label the x-axis
plt.title("Forest Area (sq. km)",fontsize=20)  #To mention the title for bar graph
#Legend shows the label names in form of a box on the upper right hand of the image
plt.legend(loc='upper right',fontsize=15)
#Saving the image of the bar graph and dpi is dots per inch 
#i.e to set the resolution of the image and to produce a clear image.
plt.savefig('Side by side bar graph2.png', dpi=144, size = 10)  
plt.show()  #To display the image of the bar graph

def carbon_dioxide_emissions(carbon_dioxide_emissions_data):
    '''
    The above function named carbon_dioxide_emissions produces a pie chart 
    of the dataset from World Bank data.
    forest_area_data: It is the dataset used for plotting the bar graph
    '''
    
    #To read the data and create a dataframe
    dataframe1 = pd.read_csv(carbon_dioxide_emissions_data, skiprows=4)
    #To select the desired rows and columns respectively
    dataframe1 = dataframe1.iloc[[35, 40, 77, 81, 109, 113, 119, 126],
                                 [0, 40, 50, 60]]
    #To drop the NaN or empty cells in the columns
    dataframe1 = dataframe1.dropna(axis=1)
    #Taking the transpose of the dataframe1
    dataframe2 = dataframe1.set_index('Country Name').T    
    return dataframe1, dataframe2
#Calling the function to read the co2 emissions dataset 
e,f = carbon_dioxide_emissions("CO2 Emissions.csv")
#Printing the variables e and f assigned to the function
print(e)  #as e = dataframe1 
print(f)  #and f = dataframe2

'''
Third visualisation: Pie chart
Plotting the pie chart using the matplotlib library by taking Country Name 
in the X axis and the years for the Y axis using the CO2 emissions dataset.
A new column named average is created and the mean of the columns is calculated using 
numpy library,i.e of the years namely 1996,2006,2016 is taken for plotting the pie chart.
'''

e["Average"] = np.mean(e, axis=1)
avg_data = e["Average"]
#To get the description of the data in the dataFrame such as mean, count, standard deviation etc
print(e.describe())
#dpi is dots per inch i.e to set the resolution of the image and to produce a clear image.
plt.figure(dpi = 144, figsize = (9,8))
#autopct is to display the percentage in the pie plot
plt.pie(avg_data, labels = e['Country Name'], autopct = "%2.2f%%")
plt.axis('equal')   #To adjust plots with equal axis aspect ratios
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
plt.title("CO2 Emissions (kt) ", fontsize=25)  #To display title of the image
#To show the label names in form of a box at the best position on the image
plt.legend(loc='best',fontsize=10)  
plt.savefig('Pie chart1.png')  #Saving the image of the pie chart.
plt.show()  #To display the image of the bar graph

def renewable_energy(renewable_energy_data):
    
    '''
    The above function named renewable_energy produces a pie chart of the dataset from World Bank data.
    renewable_energy_data: It is the dataset used for plotting the bar graph
    '''
    
    #To read the data and create a dataframe
    dataframe1 = pd.read_csv(renewable_energy_data, skiprows=4)
    #To select the desired rows and columns respectively
    dataframe1 = dataframe1.iloc[[35, 40, 77, 81, 109, 113, 119, 126],
                                 [0, 40, 50, 60]]
    #To drop the NaN or empty cells in the columns
    dataframe1 = dataframe1.dropna(axis=1)
    #Taking the transpose of the dataframe1
    dataframe2 = dataframe1.set_index('Country Name').T  
    return dataframe1, dataframe2
#Calling the function to read the renewable energy dataset 
g,h = renewable_energy("Renewable energy.csv")
#Printing the variables g and h assigned to the function
print(g)  #as g = dataframe1
print(h)   #and h = dataframe2

'''
Fourth visualisation: Pie chart
Plotting the pie chart using the matplotlib library by taking Country Name 
in the X axis and the years for the Y axis using the renewable energy dataset.
A new column named average is created and the mean of the columns is calculated using pandas library,
i.e of the years namely 1996,2006,2016 is taken for plotting the pie chart
'''

g["Average"] = g.iloc[:, 1:3].mean(axis=1)
avg_data = g["Average"]
#To get the description of the data in the dataFrame such as mean, count, standard deviation etc
print(g.describe())
#dpi is dots per inch i.e to set the resolution of the image and to produce a clear image.
plt.figure(dpi = 144, figsize = (9,8))
#autopct is to display the percentage in the pie plot
plt.pie(avg_data, labels = g['Country Name'], autopct = "%2.2f%%")  
plt.axis('equal')  #To adjust plots with equal axis aspect ratios
plt.xlabel("Countries",fontsize=25)  #To label the x-axis
plt.title("Renewable energy (%)", fontsize=25)  #To display title of the image
#To show the label names in form of a box at the best position on the image
plt.legend(loc='best',fontsize=10)
plt.savefig('Pie chart2.png')  #Saving the image of the pie chart 
plt.show()  #To display the image of the bar graph

def climate_change(climate_change_data):
    
    '''
    The above function named climate_change produces a heat map of the master dataset from the World Bank data.
    climate_change_data: It is the dataset used for plotting the bar graph
    '''
    
    #To read the data and create a dataframe
    dataframe1 = pd.read_csv(climate_change_data, skiprows = 4) 
    dataframe1 = dataframe1.fillna(0)  #To fill the NaN or empty cells with 0
    #To select 1 country i.e India from the Country Name column.
    dataframe1 = dataframe1.loc[dataframe1['Country Name'] == 'India' ]
    #4 indicators that are filtered to visualize the heatmap 
    indicator = ['Population, total','Forest area (sq. km)','CO2 emissions (kt)',
                 'Renewable energy consumption (% of total final energy consumption)']  
    filter = dataframe1['Indicator Name'].isin(indicator)
    dataframe2 = dataframe1.loc[filter]
    #Dropping the unneccessary columns
    dataframe2 = dataframe2.drop(['Country Name','Country Code','Indicator Code'],axis=1)
    #Taking the transpose of the dataframe2
    dataframe3 = dataframe2.set_index('Indicator Name').T
    dataframe3 = dataframe3.rename({'Population, total': 'Total Population', 
                                    'Forest area (sq. km)': 'Forest Area',
                                    'CO2 emissions (kt)': 'CO2 emissions',
                                    'Renewable energy consumption (% of total final energy consumption)': 'Renewable Energy'}, 
                                   axis=1)
    return dataframe1, dataframe2, dataframe3
#Calling the function to read the master dataset
x,y,z = climate_change("Master_dataset.csv")
print(z)
#Here we are using Pearson’s correlation coefficient 
correlation = z.corr(method='pearson')
print(correlation)

'''
Fifth visualisation: Heatmap of India
Plotting the heatmap using the matplotlib library by selecting the 4 indicators 
that affect the climatic changes using the climate change master dataset.
'''

fig, ax = plt.subplots(figsize=(15,10))  #Setting the size of the figure
im = ax.imshow(correlation, cmap='coolwarm', interpolation='nearest')
#Setting ticks to column names i.e xtick and ytick are the markers denoting data points on the axes.
plt.xticks(range(len(correlation.columns)), correlation.columns, fontsize = 15)
plt.yticks(range(len(correlation.columns)), correlation.columns, fontsize = 15)
plt.setp(ax.get_xticklabels(), rotation = 45, ha = "right", rotation_mode = "anchor")
cbar = ax.figure.colorbar(im, ax = ax)  #Setting the color indicator axes to the heatmap
#Creating loop over dimensions to get the annotations on the heatmap
for i in range(len(z.columns)):
    for j in range(len(z.columns)):
        text = ax.text(j, i, round(correlation.to_numpy()[i, j], 2), ha="center", 
                       va="center", color="black", fontsize = 20)
ax.set_title("India", fontsize=25)  #To display title of the image
fig.tight_layout()  #To fit the subplots
plt.savefig('Heatmap.png', dpi=144)  #Saving the image of the pie chart
plt.show()  #To display the image of the heatmap