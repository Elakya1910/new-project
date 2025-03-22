# importing the libraries
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.io as pio
pio.renderers.default = 'notebook'
import streamlit as st

# loading the datasets
df = pd.read_csv("vehicles_us.csv")

# reading the information of the datasets
print(df.info())
print(df.head())
print(df.describe())

# Check for duplicated rows
duplicate_rows = df.duplicated().sum() 
print(duplicate_rows)
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Handling missing values
df['paint_color'] = df['paint_color'].fillna('unknown')# Replacing missing paint_color with 'unknown'
df['is 4wd'] = df['is_4wd'].fillna(0)  # Replacing 2wd by 0

#Replacing missing model_year values grouped with model
df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median')) 
# Replacing missing odometer values grouped with model
df['odometer'] = df['odometer'].fillna(df.groupby(['model'])['odometer'].transform('median'))
# Replacing missing cylinders values grouped with model
df['odometer'] = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('median'))

# Visualizing the values
fig_price = px.histogram(df, x="price", title="Price Distribution")
fig_price.update_layout(yaxis_title="Number of Cars")
st.plotly_chart(fig_price)

fig_odometer = px.scatter(df, x="odometer", y="price", title="Price vs Odometer Reading")
st.plotly_chart(fig_odometer)

if st.checkbox("show data"):
   st.write(df.head())


