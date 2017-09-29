# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:48:08 2017

@author: HP
"""

v=0
dt=0.1
n=10/dt
a=1
g=-9.8
while a<=n:
    dv=g*dt
    v=v+dv
    a+=1
print(v)