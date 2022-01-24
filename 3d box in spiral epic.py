#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:49:20 2021

@author: smaran
"""
from matplotlib import pyplot as plt


#Plotting to our canvas
plt.style.use('dark_background')

plt.plot([789,5999,2000],[123,987,245],'red')
plt.plot([746,6547,5000],[345,987,768],'blue')
plt.plot([1000,2000,9000],[100,5491,321],'green')
plt.plot([700,4000,3000],[256,1100,500],'orange')
plt.plot([853,398,2935],[298,3987,634],'cyan')
plt.plot([2765,3498,8765],[145,4987,400],'yellow')


#Showing what we plotted
plt.show()