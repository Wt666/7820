import numpy as np # linear algebra
import  pandas as pd
import pandas_profiling 

# read data
data = pd.read_csv('/Users/wt/Desktop/7820/winequality_red.csv')
# 关键代码来了，就这一行代码
pandas_profiling.ProfileReport(data)
pfr = pandas_profiling.ProfileReport(data)
pfr.to_file('report1.html')