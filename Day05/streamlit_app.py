import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write',help="a", divider='rainbow')
# 加上斜體與笑臉
st.write(':blue[Hello], *World!* :sunglasses:')

st.write(1234)
# 表格展示
df = pd.DataFrame({
     'english column': ["A","B","C","D"],
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.write('這是一個 DataFrame:', df, 'Above is a dataframe.')


df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)