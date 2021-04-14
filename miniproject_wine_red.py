
import pandas as pd
import numpy as np
import os
from pandas import Series, DataFrame  # 此两个为pandas中的数据结构，特别是DataFrame
import plotly.express as px


import matplotlib.pyplot as plt
import seaborn as sns


current_color = sns.color_palette()
print(current_color)
filepath = r"C:\Users\Administrator\winequality_red.csv"
df = pd.read_csv(filepath, delimiter=";", encoding="gbk")
print(df)

sns.set_style("dark")
plt.figure(figsize = (10,8))
colnm = df.columns.to_list()[:11] + ['quality']
mcorr = df[colnm].corr()
mask = np.zeros_like(mcorr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(10,220, sep=20, as_cmap=True)
g = sns.heatmap(mcorr, mask=mask, cmap=cmap, square=True, annot=True, fmt='0.2f')
plt.show()
