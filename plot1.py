# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:02:17 2017

@author: user
"""

#Nominal Gdp
from matplotlib import pyplot as plt
years= [1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
#A graph, where years are on X-axis, and GDP is on the Y-axis.
plt.plot(years,gdp,color='green',marker ='o',linestyle='solid')
#Title Of the Graph
plt.title("Nominal GDP")
#Add a label to axis
plt.ylabel("Billions of USD")
plt.xlabel("GDP")


