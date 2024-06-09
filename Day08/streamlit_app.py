import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('滑桿')

age = st.slider("你幾歲?", 0, 130, 25)
st.write("我", age, "歲")
#####
st.subheader('限定範圍')
values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
# 0 ,100是限制 25 ,75是預設值

st.write('Values:', values)
#####
st.subheader('時間滑桿')
appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
######
st.subheader('日期滑桿')

start_time = st.slider("When do you start?",value=datetime(2020, 1, 1, 9, 30),#年/月/日/時/分
                         format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)