import streamlit as st
from joblib import load
model = load('car_price_model.joblib')




st.set_page_config(page_title=' app',layout='centered')
st.title('bu app')
st.markdown('bu markdown!')
