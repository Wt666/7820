import pandas as pd
df = pd.read_csv("/Users/wt/Documents/wine/winequality_white.csv")
df.describe()
p = df["quality"].value_counts()
print(p)

import plotly.express as px
fig = px.histogram(df,x='quality')
fig.show()

import matplotlib.pyplot as plt
for column in df.columns:
    if column!="quality":
        df_column = df[column]
        plt.scatter(df_column.index,df_column)
        plt.xlabel("index")
        plt.ylabel("value")
        plt.title(column)
        plt.show()