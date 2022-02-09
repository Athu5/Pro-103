import pandas as pd
import plotly.express as px

#reading dat from csv file
df = pd.read_csv("Copy+of+data+-+data (2).csv")
fig = px.scatter(df,x = "date",y = "cases", color = "country")
fig.show()