import streamlit as st
import pandas as pd
import os
from joblib import load
from sklearn.metrics import accuracy_score

model = load('https://github.com/jackhuntersys/AI_ML_course/blob/aec041a6f38bd339ebe7f15b4536f13362574881/3-oy/4dars/linear_model.joblib')
if model:
    print('true')


st.set_page_config(page_title=' app',layout='centered')
st.title('bu app emas fffffff')
st.markdown('bu markdown!')
st.text('sdhsdsdhshdshdhsdhshdhsdhshdhsdhshdshdhs')

print("Current dir:", os.getcwd())
print("Files:", os.listdir('.'))