import streamlit as st
import pandas as pd
import os
from joblib import load
from sklearn.metrics import accuracy_score

model = load('linear_model.joblib')
if model:
    print('true')


st.set_page_config(page_title=' app',layout='centered')
st.title('bu app emas fffffff')
st.markdown('bu markdown!')


print("Current dir:", os.getcwd())
print("Files:", os.listdir('.'))