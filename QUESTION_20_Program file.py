# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 23:55:06 2022

@author: MAHESH
"""


# Q 20) Calculate probability from the given dataset for the below cases
# Dataset: Cars.csv
# Calculate the probability of MPG of Cars for the below cases.
# MPG <- Cars $MPG
# a	P(MPG>38)
# b	P(MPG<40)
# C.P(20<MPG<50)

import pandas as pd 
df = pd.read_csv("Cars.csv")
df.shape
list(df)


W = df["MPG"].mean()
print("Mean of mpg is ",W)

# Mean of mpg is  34.422075728024666

U= df["MPG"].std()
print("Standad Divation of mpg is ",U)

# Standad Divation of mpg is  9.131444731795982

from scipy.stats import norm
nd=norm(34.4220,9.13144)       # mean,sd

# a) P(MPG>38

X1 = nd.cdf(38)
X1=1-nd.cdf(38)
print("the probability of P (MPG<38) is",X1)

# b	P(MPG<40)

X2=nd.cdf(39)
print("the probability of 	P(MPG<40) is",X2)

# C.P(20<MPG<50)

X3 = nd.cdf(20)
X3

X4 = nd.cdf(50)
X4


X5 = X4-X3
print("the probability of P (20<MPG<50) is",X5)




