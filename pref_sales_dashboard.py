import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv('sales_data.csv')

# ダッシュボードのタイトル
st.title('都道府県別売上ダッシュボード')

# データの表示
st.subheader('売上データ')
st.write(data)

# 都道府県別の売上でフィルタリングするためのスライダー
sales_filter = st.slider('売上でフィルタリング', 0, 400, 200)

# フィルタリングされたデータの表示
filtered_data = data[(data['sales'] >= sales_filter)]
st.subheader('フィルタリングされたデータ')
st.write(filtered_data)

# フィルタリングされたデータのグラフ
st.subheader('売上の棒グラフ')
fig, ax = plt.subplots()
ax.bar(filtered_data['prefecture'], filtered_data['sales'])
ax.set_xlabel('prefecture')
ax.set_ylabel('Sales')
ax.set_title('Sales by Prefecture')
st.pyplot(fig)