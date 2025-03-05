import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")

var_str = ""
var_us = "USA"
var_it = "Italy"
var_br = "Brazil"
var_hello = "Hello World Real:"
 
list_1 = [var_hello, var_us, var_it, var_br]


for x in list_1 :
    var_str = var_str + x + " "
    
st.write(var_str)

st.divider()

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
v_price_max = df_top_100_books["book price"].max()
v_price_min = df_top_100_books["book price"].min()
v_max_price = st.sidebar.slider("Price Range", v_price_min, v_price_max, v_price_max, )

df_books = df_top_100_books[df_top_100_books["book price"] <= v_max_price]
st.write(df_books)

v_graph1 = px.bar(df_books["year of publication"].value_counts())
v_graph2 = px.bar(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(v_graph1)
col2.plotly_chart(v_graph2)
