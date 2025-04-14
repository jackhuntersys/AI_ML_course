import streamlit as st
from joblib import load
model = load('car_price_model.joblib')




st.set_page_config(page_title='Yomgirni bashorat qilish uchun app',layout='centered')
st.title('Ob xavo:Yomgir')
st.markdown('Bugungi ob xavo malumotlarini kiriting va yomgirni bizning app yordamida bashorat qiling!')