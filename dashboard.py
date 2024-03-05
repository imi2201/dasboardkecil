import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

seller_df = pd.read_csv(https://'raw.githubusercontent.com/imi2201/dasboardkecil/main/seller_order.csv')
product_df = pd.read_csv(https://'raw.githubusercontent.com/imi2201/dasboardkecil/main/product_items.csv')

#main title
st.title('Dashboard E-Commerce')

# Create two columns
col1, col2 = st.columns(2)

# Display seller data in the first column
with col1:
    st.write("Seller Data")
    st.write(seller_df)

# Display product data in the second column
with col2:
    st.write("Product Data")
    st.write(product_df)
