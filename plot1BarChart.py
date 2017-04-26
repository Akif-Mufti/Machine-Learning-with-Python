# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:02:17 2017

@author: user
"""

#Nominal BAr
from matplotlib import pyplot as plt
movies=["DarkKnight","RobinHood","Slavery","Alice","Alice34","Alicemmmm"]
Awards= [3,6,1,9,19,1]
#bars by default are of width 0.8 , so we will add 0.1 to the left coordinates
#So that each bar is centered
xs=[i for i,_ in enumerate(movies)]
#plot bars with left x cordinates [xs],heights [awards]
plt.bar(xs,Awards)
plt.ylabel("Number Of Awards")
plt.title("My favourite Movie")
#label x axis with movie names at bar
plt.xticks([i for i,_ in enumerate(movies)],movies)
plt.show()


