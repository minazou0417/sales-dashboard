import streamlit as st

# サイドバーにタイトルを追加
st.sidebar.title('設定')

# サイドバーにチェックボックスを追加
show_data = st.sidebar.checkbox('データを表示する')

# サイドバーにラジオボタンを追加
theme = st.sidebar.radio('テーマを選択してください', ['ライト', 'ダーク'])

# メインコンテンツ
st.title('サイドバーの活用例')

if show_data:
    st.write('データが表示されています。')

st.write(f'選択されたテーマ: {theme}')