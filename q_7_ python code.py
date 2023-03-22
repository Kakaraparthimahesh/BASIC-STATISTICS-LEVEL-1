# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:15:25 2022

@author: MAHESH
"""


import pandas as pd
df = pd.read_csv("D:/ALL ASSIGNMENT/BASIC STATISTICS_LEVEL 1/Q7.csv")
df
df.shape
list(df)

import matplotlib.pyplot as plt

df["Points"]
df["Score"]
df["Weigh"]

# HISTOGRAM

plt.hist(df["Points"])
plt.hist(df["Score"])
plt.hist(df["Weigh"])



