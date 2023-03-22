# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:23:34 2022

@author: MAHESH
"""
# Q9_a.csv

import pandas as pd
df = pd.read_csv("D:/ALL ASSIGNMENT/BASIC STATISTICS_LEVEL 1/Q9_a.csv")
pd.set_option("display.max_columns", 50)
df.shape
list(df)

from scipy.stats import kurtosis,skew

kurt = kurtosis(df[["speed","dist"]], fisher = False)
print ("kurtosis:",kurt) 

sk=skew(df[["speed","dist"]])
print("skewness:",sk) 

import matplotlib.pyplot as plt

df["speed"]
df["dist"]

# HISTOGRAM

plt.hist(df["speed"])
plt.hist(df["dist"])

# Q9_b.csv

df = pd.read_csv("D:/ALL ASSIGNMENT/BASIC STATISTICS_LEVEL 1/Q9_b.csv")
pd.set_option("display.max_columns", 50)
df.shape
list(df)

kurt = kurtosis(df[["SP","WT"]], fisher = False)
print ("kurtosis:",kurt) 

import matplotlib.pyplot as plt

df["SP"]
df["WT"]

# HISTOGRAM

plt.hist(df["SP"])
plt.hist(df["WT"])

