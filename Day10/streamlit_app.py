import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     '你最喜歡的顏色是什麼?',
     ('藍', '紅', '綠'))

st.write('你最喜歡的顏色是 ', option ,"色")