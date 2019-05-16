# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:23:23 2018

@author: hasna
"""
principal = (int(input("what is the principal amount:")))
annualcontrib = (int(input("what amount do you add per year:")))
growthrate = 1.05
years = (int(input("how many years do you want to invest:")))
def constantinvestment(principal, annualcontrib,growthrate, years):
    invest = (principal + annualcontrib)*growthrate
    for i in range(1,years):
        invest = (invest + annualcontrib)*growthrate
    return invest 
print(constantinvestment(principal, annualcontrib,growthrate, years))
        
