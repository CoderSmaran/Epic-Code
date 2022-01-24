#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:44:36 2021

@author: smaran
"""


from matplotlib import pyplot as plt

plt.style.use('dark_background')
import random

for x in range(50):
    
       
    a=random.randint(200,3000)
    b=random.randint(300,7000)
    c=random.randint(100,9000)
    d=random.randint(400,5000)
   

    plt.plot([a,b,c],[a+b,987,245],'red')
    plt.plot([746+c,632+b,700+a],[345,987,768],'blue')
    plt.plot([c,c+a,a+c],[a,b+c,b],'green')
    plt.plot([b,d,c+a],[d+a,b+a,c+d],'orange')
    plt.plot([c+a,d+a,d+b],[a+b,c+d,a],'cyan')
    plt.plot([2765,d,a+b+c],[145,d+c-b,400],'yellow')
    plt.show()
    plt.clf()


#Showing what we plotted
plt.show()