# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:06:16 2018

@author: hasna
"""
principal = (float(input("what is the principal amount:")))
annualcontrib = (float(input("what amount do you add per year:")))
growthrate =[1.05,1.03,1.015,1.045,1.06]
years = (int(input("how many years do you want to invest:")))
def constantinvestment(principal, annualcontrib,growthrate, years):
    invest = (principal + annualcontrib)*growthrate[0]
    for i in range(1,years):
            invest = (invest + annualcontrib)*growthrate[i]
    return invest 
print(constantinvestment(principal, annualcontrib,growthrate, years))
