# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 03:16:45 2018

@author: hasna
"""
upper = int(input("enter upper bound:")) 
lower = int(input("enter lower bound:"))
list1 = [8,3,11,5,2,21,38,1,7]
list2 = []
"""
GetMembersinrange
This function displays the numbers in the list between the upper and lower bounds
Parameter: list name, lower bound, upper bound
"""
def GetMembersinrange(list1,lower,upper): #while i is between 0 and the length of the list
    for i in range(0,len(list1)):           
        if lower <= list1[i] <= upper:  #and if the value at index i is between the lower and upper bound
            list2.append(list1[i]) #add value to list2
        else: 
            i = i + 1 #increment i by 1 
    return list2 #return new list2
print(GetMembersinrange(list1,lower,upper)) #print list2 

            
