import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("others/datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("others/datasets/Top-100 Trending Books.csv")

v_books = df_top_100_books["book title"].unique()
v_book_sel = st.sidebar.selectbox("Books: ", v_books)

df_books = df_top_100_books[df_top_100_books["book title"] == v_book_sel]
df_reviews_f = df_reviews[df_reviews["book name"] == v_book_sel]

v_book_title  = df_books["book title"].iloc[0]
v_book_genre  = df_books["genre"].iloc[0]
v_book_price  = f"${df_books['book price'].iloc[0]}"
v_book_rating = df_books["rating"].iloc[0]
v_book_year   = df_books["year of publication"].iloc[0]

st.title(v_book_title)
st.subheader(v_book_genre)
col1,col2,col3 = st.columns(3)
col1.metric("Price", v_book_price)
col2.metric("Rating", v_book_rating)
col3.metric("Year", v_book_year)

st.divider()
st.subheader("Reviews: ")

for rows in df_reviews_f.values : 
    v_message = st.chat_message(f"{rows[4]}")
    v_message.write(f"**{rows[2]}**")
    v_message.write(rows[5])
