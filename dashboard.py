import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

seller_df = pd.read_csv('https://raw.githubusercontent.com/imi2201/dasboardkecil/main/seller_order.csv')
product_df = pd.read_csv('https://raw.githubusercontent.com/imi2201/dasboardkecil/main/product_items.csv')

#main title
st.title('Dashboard E-Commerce')

# Create two columns
col1, col2 = st.column(2)

# Display seller data in the first column
with col1:
    st.write("Seller Data")
    st.write(seller_df)

# Display product data in the second column
with col2:
    st.write("Product Data")
    st.write(product_df)

st.write("diberikan data tersebut akan di cari:")
col3,col4 = st column(2)

with col3:
    st.write("pertanyaan 1 akan ditunjukkan 10 product")
    st.write("yang memiliki tingkat pembelian tertinggi")
    category_counts = product_df.groupby("product_category_name")["order_id"].count()
    top_categories = category_counts.sort_values(ascending=False).head(10)
    plt.barh(y=top_categories.index, width=top_categories.values)
    plt.xlabel('Count')  # Label for x-axis
    plt.ylabel('Product Category')  # Label for y-axis
    plt.title('Top 10 Product Ordered')
    st.pyplot(plt)
    plt.clf()
