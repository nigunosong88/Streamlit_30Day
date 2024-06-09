import streamlit as st
import time

st.title('st.progress')

with st.expander('這一個例子'):
     st.write('您現在可以使用”st.progress“命令在 Streamlit 應用程式中顯示計算進度。')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
st.button("Rerun")