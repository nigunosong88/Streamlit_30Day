import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     '你最喜歡的顏色是什麼?',
     ['藍', '紅', '綠', '黃'], # 選項
     ['藍', '紅'])# 預設值

st.write('你喜歡的顏色是:', options)

