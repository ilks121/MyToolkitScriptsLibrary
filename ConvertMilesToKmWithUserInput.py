#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:01:56 2017

@author: ilkay
"""

def miles_to_km(miles):
    km = miles * 1.60934
    print(miles,"miles =",km,"km")
    
m = input("Please enter miles: ")
m = float(m)
miles_to_km(m)
