import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import seaborn as sns



# layout the tiles

df = pd.DataFrame(columns=['State', 'Position', 'Party', 'X', 'Y'])

df.loc[df.shape[0]] = ['WA', 1, 'LIB', 4, 4]
df.loc[df.shape[0]] = ['WA', 2, 'LIB', 3, 5]
df.loc[df.shape[0]] = ['WA', 3, 'LIB', 4, 5]
df.loc[df.shape[0]] = ['WA', 4, 'LIB', 3, 6]
df.loc[df.shape[0]] = ['WA', 5, 'LIB', 4, 6]
df.loc[df.shape[0]] = ['WA', 6, 'LIB', 3, 7]
df.loc[df.shape[0]] = ['WA', 7, 'GRN', 4, 7]
df.loc[df.shape[0]] = ['WA', 8, 'GRN', 3, 8]
df.loc[df.shape[0]] = ['WA', 9, 'ALP', 4, 8]
df.loc[df.shape[0]] = ['WA', 10, 'ALP', 3, 9]
df.loc[df.shape[0]] = ['WA', 11, 'ALP', 4, 9]
df.loc[df.shape[0]] = ['WA', 12, 'ALP', 4, 10]

df.loc[df.shape[0]] = ['NT', 1, 'ALP', 5, 11]
df.loc[df.shape[0]] = ['NT', 2, 'CLP', 5, 10]

df.loc[df.shape[0]] = ['SA', 1, 'LIB', 5, 9]
df.loc[df.shape[0]] = ['SA', 2, 'LIB', 5, 8]
df.loc[df.shape[0]] = ['SA', 3, 'LIB', 6, 9]
df.loc[df.shape[0]] = ['SA', 4, 'LIB', 6, 8]
df.loc[df.shape[0]] = ['SA', 5, 'LIB', 6, 7]
df.loc[df.shape[0]] = ['SA', 6, 'GRN', 7, 9]
df.loc[df.shape[0]] = ['SA', 7, 'RPT', 7, 8]
df.loc[df.shape[0]] = ['SA', 8, 'ALP', 7, 7]
df.loc[df.shape[0]] = ['SA', 9, 'CA', 5, 7]
df.loc[df.shape[0]] = ['SA', 10, 'ALP', 6, 6]
df.loc[df.shape[0]] = ['SA', 11, 'ALP', 7, 6]
df.loc[df.shape[0]] = ['SA', 12, 'ALP', 7, 5]

df.loc[df.shape[0]] = ['Qld', 1, 'LNP', 11, 10]
df.loc[df.shape[0]] = ['Qld', 2, 'LNP', 8, 10]
df.loc[df.shape[0]] = ['Qld', 3, 'LNP', 9, 10]
df.loc[df.shape[0]] = ['Qld', 4, 'LNP', 10, 10]
df.loc[df.shape[0]] = ['Qld', 5, 'LNP', 10, 12]
df.loc[df.shape[0]] = ['Qld', 6, 'LNP', 8, 9]
df.loc[df.shape[0]] = ['Qld', 7, 'GRN', 9, 9]
df.loc[df.shape[0]] = ['Qld', 8, 'ONP', 10, 9]
df.loc[df.shape[0]] = ['Qld', 9, 'ONP', 11, 9]
df.loc[df.shape[0]] = ['Qld', 10, 'ALP', 12, 9]
df.loc[df.shape[0]] = ['Qld', 11, 'ALP', 10, 11]
df.loc[df.shape[0]] = ['Qld', 12, 'ALP', 13, 9]

df.loc[df.shape[0]] = ['NSW', 1, 'LNP', 8, 8]
df.loc[df.shape[0]] = ['NSW', 2, 'ALP', 9, 8]
df.loc[df.shape[0]] = ['NSW', 3, 'LNP', 10, 8]
df.loc[df.shape[0]] = ['NSW', 4, 'ALP', 11, 8]
df.loc[df.shape[0]] = ['NSW', 5, 'LNP', 12, 8]
df.loc[df.shape[0]] = ['NSW', 6, 'ALP', 13, 8]
df.loc[df.shape[0]] = ['NSW', 7, 'GRN', 12, 7]
df.loc[df.shape[0]] = ['NSW', 8, 'LNP', 9, 7]
df.loc[df.shape[0]] = ['NSW', 9, 'ALP', 10, 7]
df.loc[df.shape[0]] = ['NSW', 10, 'LNP', 11, 7]
df.loc[df.shape[0]] = ['NSW', 11, 'LNP', 13, 7]
df.loc[df.shape[0]] = ['NSW', 12, 'GRN', 14, 8]

df.loc[df.shape[0]] = ['ACT', 1, 'ALP', 14, 7]
df.loc[df.shape[0]] = ['ACT', 2, 'LIB', 13, 6]

df.loc[df.shape[0]] = ['Vic', 1, 'LIB', 8, 6]
df.loc[df.shape[0]] = ['Vic', 2, 'LIB', 8, 5]
df.loc[df.shape[0]] = ['Vic', 3, 'LIB', 9, 6]
df.loc[df.shape[0]] = ['Vic', 4, 'LIB', 9, 5]
df.loc[df.shape[0]] = ['Vic', 5, 'LIB', 10, 6]
df.loc[df.shape[0]] = ['Vic', 6, 'NAT', 8, 7]
df.loc[df.shape[0]] = ['Vic', 7, 'GRN', 10, 5]
df.loc[df.shape[0]] = ['Vic', 8, 'GRN', 11, 5]
df.loc[df.shape[0]] = ['Vic', 9, 'ALP', 12, 5]
df.loc[df.shape[0]] = ['Vic', 10, 'ALP', 12, 6]
df.loc[df.shape[0]] = ['Vic', 11, 'ALP', 13, 5]
df.loc[df.shape[0]] = ['Vic', 12, 'ALP', 11, 6]


df.loc[df.shape[0]] = ['Tas', 1, 'LIB', 13, 1]
df.loc[df.shape[0]] = ['Tas', 2, 'LIB', 9, 4]
df.loc[df.shape[0]] = ['Tas', 3, 'LIB', 10, 4]
df.loc[df.shape[0]] = ['Tas', 4, 'LIB', 11, 4]
df.loc[df.shape[0]] = ['Tas', 5, 'LIB', 12, 4]
df.loc[df.shape[0]] = ['Tas', 6, 'GRN', 13, 4]
df.loc[df.shape[0]] = ['Tas', 7, 'GRN', 12, 2]
df.loc[df.shape[0]] = ['Tas', 8, 'JLP', 13, 2]
df.loc[df.shape[0]] = ['Tas', 9, 'ALP', 10, 3]
df.loc[df.shape[0]] = ['Tas', 10, 'ALP', 11, 3]
df.loc[df.shape[0]] = ['Tas', 11, 'ALP', 12, 3]
df.loc[df.shape[0]] = ['Tas', 12, 'ALP', 13, 3]


color_dict = {'Vic': '#000099', 'ACT': 'orange', 'NSW': '#99ccff', 'Qld': 'maroon', 'Tas': '#33cc33', 'SA': '#ff0000', 'NT': 'goldenrod', 'WA': 'black'}
df['Color'] = df['State'].apply(lambda x: color_dict[x])

color_dict = {'ALP': 'red', 'LIB': 'blue', 'LNP': '#3366FF', 'NAT': '#196F3D', 'GRN': '#00CC00', 'JLP': '#ffcc66', 'ONP': 'grey', 'CLP': 'goldenrod', 'RPT': 'grey', 'CA': 'grey', 'JLP': 'grey'}
df['Color'] = df['Party'].apply(lambda x: color_dict[x])




# plot the tiles

size_x = 888
padding_x = 20
padding_offset = (size_x * 0.1) / padding_x

fig = alt.Chart(df, title='Full Australian Senate tilemap (square) ').mark_square(size=(size_x * padding_offset) ).encode(
    x=alt.X("X", scale=alt.Scale(domain=[2, 15])),
    y=alt.Y("Y", scale=alt.Scale(domain=[0, 13])),
    color=alt.Color("Color", scale=None),
    tooltip=['State', 'Party'], 
).properties(height=size_x, width=size_x).configure_title(fontSize=24,  anchor='start').configure_axis(labels=False, ticks=False, title=None, domain=False, grid=False)

st.write(fig)
