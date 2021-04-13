import pandas as pd
df = pd.read_csv("/Users/wt/Documents/wine/winequality_red.csv")
df.describe()
q = df["quality"].value_counts()
print(q)

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