import streamlit as st
import pandas as pd
import os
from joblib import load
from sklearn.metrics import accuracy_score

model = load('https://github.com/jackhuntersys/AI_ML_course/blob/25a1f70bd658d096fd3a79bbbfc691e77626d90a/3-oy/4dars/model.joblib')


st.set_page_config(page_title=' app',layout='centered')
st.title('bu app emas fffffff')
st.markdown('bu markdown!')
MODEL_PATH = 'car_price.joblib'

if os.path.exists(MODEL_PATH):
    model = load(MODEL_PATH)
else:
    st.error(f"Model file '{MODEL_PATH}' not found. Please upload it to continue.")
    st.stop()