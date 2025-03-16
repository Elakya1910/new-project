import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv("vehicles_us.csv")
st.header("Vehicle Sales Analysis")
fig = px.histogram(df,x="price")
st.plotly_chart(fig)
fig = px.scatter(df,x="fuel", y="type")
st.plotly_chart(fig)
if st.checkbox("show data"):
   st.write(df.head())


