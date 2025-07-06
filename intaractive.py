import streamlit as st
import requests

def fetch_data_with_error_handling():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTPエラーが発生しました: {http_err}")
    except Exception as err:
        st.error(f"予期しないエラーが発生しました: {err}")
    return None

# データの取得
data = fetch_data_with_error_handling()

# データの表示
if data:
    st.write("取得したデータの一部を表示します:")
    st.json(data[:5])