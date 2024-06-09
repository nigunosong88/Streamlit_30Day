import streamlit as st

st.title('st.form')

st.header('1. Example of using `with` notation')

with st.form('my_form'):
    st.subheader('**Order your tea**')

    tea_val = st.selectbox('茶', ['綠茶', '紅茶'])
    sugar_val = st.selectbox('糖', ['全糖', '半糖', '無糖'])
    ice_val = st.selectbox('冰塊', ['全冰', '少冰', '去冰'])
    milk_val = st.select_slider('牛奶', ['None', 'Low', 'Medium', 'High'])
    cup_val = st.checkbox('大杯')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ 你的選擇:
        - 茶: `{tea_val}`
        - 糖: `{sugar_val}`
        - 冰: `{ice_val}`
        - 牛奶: `{milk_val}`
        - 大杯: `{cup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)