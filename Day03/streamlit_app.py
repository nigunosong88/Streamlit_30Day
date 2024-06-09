import streamlit as st

st.header('st.button')
st.write('按鈕範例')

if st.button('按鈕'):
     st.write('按下')
else:
     st.write('未按下')