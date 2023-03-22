# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 23:08:12 2022

@author: MAHESH
"""

#confidence intervals
 
from scipy import stats
import numpy as np

df_ci=stats.norm.interval(0.94,loc=200,scale=30)
print("gain at 94% confidence interval is:",np.round(df_ci))
print("94% of confidence interval is :",np.round(df_ci,4))

df_ci=stats.norm.interval(0.98,loc=50,scale=5)
print("gain at 98% confidence interval is:",np.round(df_ci))
print("98% of confidence interval is :",np.round(df_ci,4))

df_ci=stats.norm.interval(0.96,loc=50,scale=5)
print("gain at 96% confidence interval is:",np.round(df_ci))
print("96% of confidence interval is :",np.round(df_ci,4))




# 94% of confidence interval is : [143.5762 256.4238]
# 95% of confidence interval is : [38.3683 61.6317]
# 96% of confidence interval is : [39.7313 60.2687]



