import streamlit as st
from joblib import load

model = load('car_price_model.h5')


st.set_page_config(page_title=' app',layout='centered')
st.title('bu app emas')
st.markdown('bu markdown!')
