import streamlit as st

st.header('st.checkbox')

st.write ('請問你要訂購什麼? (複選)')

icecream = st.checkbox('冰淇淋')
coffee = st.checkbox('咖啡')
cola = st.checkbox('可樂')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

