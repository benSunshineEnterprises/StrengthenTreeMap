import squarify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
import plotly.express as px
import textwrap
import plotly.graph_objects as go

def customwrap(s,width=15):
    return "<br>".join(textwrap.wrap(s,width=width))

df = pd.read_csv('strengthens.csv')# convert to numeric and drop na
df["Strengthen"]= df.Strengthen.map(customwrap)
sum = sum(df["Number"])
df["percent"]=(df["Number"]/sum)*100
percent=df["percent"]
fig = px.treemap(df, 
                 path=['Strengthen'], 
                 values='Number',
                 color='Number',
)
fig.update_layout(
    font=dict(
        family="Arial",
        color="RebeccaPurple",
        size=18,
    ),
    uniformtext_minsize=16, 
)
fig.update_traces(
    texttemplate = "%{label}: %{value:s}",                

)
fig.data[0].hovertemplate = 'Strengthen: %{label}<br>Number: %{value}'
fig.show()




