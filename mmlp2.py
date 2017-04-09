# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:11:14 2017

@author: user
"""

# define an array
import numpy
mylist = [1, 2, 3]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
import numpy
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print( myarray[0])
print( myarray[-1])
print(myarray[0, 2])
print(myarray[:, 2])
#print("First row: %s") % myarray[0]
#print("Last row: %s") % myarray[-1]
#print("Specific row and col: %s") % myarray[0, 2]
#print("Whole col: %s") % myarray[:, 2]

#Airthmetic
# arithmetic

myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 3, 3])
print(myarray1 + myarray2)
print(myarray1 * myarray2)