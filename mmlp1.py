# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:17:39 2017

@author: user Aakif Mairaj
"""

# Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)

value = 123.1
print(value)
value = 10
print(value)
# Boolean
a = True
b = False
print(a, b)
# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)
# No value
a = None
print(a)
value = 99
if value == 99:
    print('hi how are u')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe') 
 # For-Loop
for i in range(19):
    print(i)
# While-Loop
i = 0
while i < 10:
    print(i)
    i += 1

a = (1, 2, 3)
print(a)
#List
mylist = [1, 2, 3] 
#print("Zeroth Value: "%d") % mylist[0]
mylist.append(4)
#print("List Length: "%d") % len(mylist)
for v in mylist:
    print(v)
#mydict = {'a': 1, 'b': 2, 'c': 3}
#print("A value: %d") % mydict['a']
#mydict['a'] = 11 
#print("A value: %d") % mydict['a']
#print("Keys: %s") % mydict.keys()
#print("Values: %s") % mydict.values()
#for key in mydict.keys():
#          print(mydict[key])
# Sum function
def mysum(x, y):
    return(x + y)
# Test sum function
result = mysum(1, 3)
print(result)

