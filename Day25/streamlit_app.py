import streamlit as st

st.title('st.session_state')

def F_to_C():
  st.session_state.f = st.session_state.c*9/5+32
def C_to_F():
  st.session_state.c = (st.session_state.f-32)*5/9

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  C = st.number_input("攝氏:", key = "c", on_change = F_to_C)
with col2:
  F = st.number_input("華氏:", key = "f", on_change = C_to_F)

st.header('Output')
st.write("st.session_state object:", st.session_state)