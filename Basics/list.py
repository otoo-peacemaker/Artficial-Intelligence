# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:02:35 2020

@author: Kwesi_Welbred
"""

"""
List is a collection of items of any kind(thus, it accepts any type of data).
The items are enclosed by square blacket and assgned to any variable name.
The elements in the list are accessed by indexing either by negative or positive index, depending the
element you want to access.

Programmers mostly use the negative indexing if they want to select a particular element
from the end of the list.

Follow the Tutorials as we begin. 
"""

myList = [2,5,6,'Kwesi','Yaw','Yaa','Agness']# declare the list
myList[0] # access the first item
myList[-1] # access the last but one item

#ask python to show you which built-in operational function can be perform on the list

dir(myList)
"""
The output

 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
"""
help(myList.sort)# Help on built-in function sort:
len(myList)#the length of the list




"""
slicing, the process of selecting a particular group of items in a particular range
use colon to slice 
eg myList[:]. this means select everything from the begining to the end.
eg2.
"""
myList[0 :-1]
myList[-3:-1]
myList[:-1]
 

