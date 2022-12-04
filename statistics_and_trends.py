# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:09:06 2022

@author: Aroma
"""

import pandas as pd  #To open the files
import matplotlib.pyplot as plt  #Used for vizualizations

def Population(reading_the_file):
        dataframe1 = pd.read_csv(reading_the_file,skiprows=4) #first read the data,convert to dataframe
        dataframe1 = dataframe1.iloc[113:120, [0,5,10,15,20,25]]
        dataframe2 = dataframe1.T
        print(dataframe1)
        print(dataframe2)
        
        dataframe1.plot(kind="bar", x = 'Country Name', rot=0)
        
        plt.xlabel("Countries")  #To label the x-axis
        #plt.ylabel("Urban Population (%)")  #To label the y-axis
        plt.title("Urban Population (%)") #To mention the title for stacked bar graph
        plt.legend(loc='upper right')  #To show the label names in form of a box
        plt.savefig('Side by side bar graph.png') #Saving the image of the line graph
        plt.show()  #To display the image of the line graph
        #plt.xticks(rotation=5)
        return dataframe1, dataframe2
    
print(Population("Urban population.csv"))