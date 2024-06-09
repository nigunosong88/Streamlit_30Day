import streamlit as st

st.title('自訂 Streamlit 應用程式的主題')

st.write('在資料夾內加入 `.streamlit/config.toml`')

st.code("""
[theme]
primaryColor="#F39C12"                  # 滑條顏色
backgroundColor="#2E86C1"               # 背景顏色
secondaryBackgroundColor="#AED6F1"      # 側面背景色
textColor="#FFFFFF"                     # 文字顏色
font="monospace"                        # 等寬字體
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)