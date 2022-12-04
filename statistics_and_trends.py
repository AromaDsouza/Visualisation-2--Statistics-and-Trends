# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:09:06 2022

@author: Aroma
"""

import pandas as pd  #To open the files
import matplotlib.pyplot as plt  #Used for vizualizations

def urban_population(reading_the_file):
        dataframe1 = pd.read_csv(reading_the_file,skiprows=4) #first read the data,convert to dataframe
        #dataframe1 = dataframe1.iloc[11:20,[0,40,50,60]]
        dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
        dataframe1 = dataframe1.fillna(0)
        dataframe2 = dataframe1.T
        print(dataframe1)
        print(dataframe2)
        
        plt.figure(figsize=(20,10),dpi=144)
        plt.plot(dataframe1['Country Name'],dataframe1["1986"],label="1996")
        plt.plot(dataframe1['Country Name'],dataframe1["1996"],label="2006")
        plt.plot(dataframe1['Country Name'],dataframe1["2006"],label="2006")
        plt.plot(dataframe1['Country Name'],dataframe1["2016"],label="2016")
        plt.xlabel("Countries",fontsize=25)  #To label the x-axis
        #plt.ylabel("Urban Population (%)")  #To label the y-axis
        plt.xticks(rotation=45)
        plt.title("Urban Population (%)",fontsize=25) #To mention the title for stacked bar graph
        plt.legend(loc='upper right',fontsize=20)  #To show the label names in form of a box
        plt.savefig('Line graph.png') #Saving the image of the line graph
        plt.show()
      
print(urban_population("Urban population.csv"))

def green_house_gases(read_the_file):
        dataframe1 = pd.read_csv(read_the_file,skiprows=4) #first read the data,convert to dataframe
        dataframe1 = dataframe1.iloc[111:120, [0,20,30,40,50,60]]       
        #dataframe1 = dataframe1.filter(items=[10,22,35,40,77,81,109,119], axis=0)
        dataframe1 = dataframe1.fillna(0)
        dataframe2 = dataframe1.T
        print(dataframe1)
        print(dataframe2)
        
        dataframe1.plot(kind="bar", x = 'Country Name', rot=0, figsize= (20,20))
        plt.xlabel("Countries",fontsize=25)  #To label the x-axis
        #plt.ylabel("Urban Population (%)")  #To label the y-axis
        plt.title("Urban Population (%)",fontsize=25) #To mention the title for stacked bar graph
        plt.legend(loc='upper right',fontsize=20)  #To show the label names in form of a box
        plt.savefig('Side by side bar graph.png') #Saving the image of the line graph
        plt.show()  #To display the image of the line graph
        #plt.xticks(rotation=5)
        return dataframe1, dataframe2   
     
print(green_house_gases("Greenhouse gases.csv"))