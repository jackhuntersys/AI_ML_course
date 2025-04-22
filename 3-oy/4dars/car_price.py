import streamlit as st
import pandas as pd
import os
from joblib import load
from sklearn.metrics import accuracy_score

model = load('3-oy/4dars/linear_model.joblib')
if model:
    print('true')
print("Current dir:", os.getcwd())
print("Files:", os.listdir('.'))


st.set_page_config(page_title='Audi car price',layout='centered')
st.title('Calculate your used car price')
model_name = st.text_input('Car model')
year = st.number_input("Enter a year", min_value=1900, max_value=2100, value=2025, step=1)
transmission = st.selectbox("Transmission", ["Manual", "Automatic", "Semi-Auto"])
mileage = st.number_input("Mileage")
fuel = st.selectbox("Fuel type", ['Diesel', 'Petrol', 'Hybrid'])
tax = st.number_input('Tax')
mpg = st.number_input('MPG', 0.0)
engine = st.number_input('Engine size', 0.0)


input_data = pd.DataFrame([{
    'model': model_name,
    'year' : year,
    'transmission': transmission,
    'mileage': mileage,
    'fuelType': fuel,
    'tax':tax,
    'mpg':mpg,
    'engineSize': engine
}])
