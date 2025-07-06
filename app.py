import streamlit as st
import pandas as pd

# CSVファイルの読み込み
data = pd.read_csv('sample_data.csv')

# タイトルの表示
st.title('ユーザー入力によるデータのフィルタリング')

# ユーザー入力によるフィルタリング
city_filter = st.selectbox('都市でフィルタリング', data['city'].unique())
age_filter = st.slider('年齢でフィルタリング', 0, 100, 30)

# フィルタリングされたデータの表示
filtered_data = data[(data['city'] == city_filter) & (data['age'] >= age_filter)]
st.write(filtered_data)