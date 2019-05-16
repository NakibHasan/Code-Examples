# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 03:34:21 2018

@author: hasna
"""
list1 = [8,3,11,5,2,21,38,1,7]
list2 = []
"""
removeeven
This function displays the numbers in the list that are odd
Parameter: list name
"""
def removeeven(list1): 
    for i in range(0,len(list1)): #while i is between 0 and length of list
        if list1[i] % 2 != 0:  # and if the value at index i is even 
            list2.append(list1[i]) #add value to list2 
        else: 
            i = i + 1 #increment
    return list2 #return list2 
print(removeeven(list1))
