# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:31:13 2017

@author: HP
"""

import time,os

a1=["#   #   ###    ###"]
a2=[" # #   #        # "]
a3=["  #     ##      # "]
a4=[" # #       #  # # "]
a5=["#   #   ###   ### "]

t=0
a=1
b=0
while t<100:
    os.system('cls')
    for i1 in a1:
        print(i1,end='')
    print("\n")
    for i2 in a2:
        print(i2,end='')
    print("\n")
    for i3 in a3:
        print(i3,end='')
    print("\n")
    for i4 in a4:
        print(i4,end='')
    print("\n")
    for i5 in a5:
        print(i5,end='')
    print("\n")
    for j in (a1,a2,a3,a4,a5):
        j.insert(0," ")
    time.sleep(a**0.5-b**0.5) #感谢刘肇宁同学想出的办法，把时间T写成了两个变量的函数，从而可以把程序写成循环
    a+=1
    b+=1
    t+=1
   