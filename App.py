import streamlit as st 
import numpy as np 
import pandas as pd  
import pickle 
from xgboost import XGBClassifier

with open('Final_model_xgb.pkl','rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    input_data = np.array(input_data, dtype='object')
    pred = model.predict_proba(input_data)[:, 1][0]
    
    if pred > 0.5:
        return f'This Booking is more likely to get cancelled: Chances={round(pred * 100, 2)}%'
    else:
        return f'This Booking is less likely to get cancelled: Chances={round(pred * 100, 2)}%'

def main():
    st.title('INN Hotels')
    st.image('hotelimage.jpg', use_column_width=True)
    
    lt = st.text_input('Enter Lead time')
    mkt = (lambda x: 1 if x == 'Online' else 0)(st.selectbox('Enter the type of booking', ['Online', 'Offline']))
    spcl = st.selectbox('How many special requests have been made?', [0, 1, 2, 3, 4, 5])
    price = st.text_input('Enter the price of the room.')
    adults = st.selectbox('How many Adults per room?', [1, 2, 3, 4])
    wknd = st.text_input('How many weekend nights?')
    prk = (lambda x: 1 if x == 'Yes' else 0)(st.selectbox('Does booking include parking facility?', ['Yes', 'No']))
    wk = st.text_input('How many weekday nights')
    
    # Use date_input to get the arrival date
    arr_d = st.date_input('What will be the date of arrival.')
    
    # Extract the day, month, and weekday from arr_d
    arr_day = arr_d.day  # Day of the month
    arr_month = arr_d.month  # Month
    arr_weekday = arr_d.weekday()  # Weekday (0 = Monday, 6 = Sunday)

    # Mapping weekday (0=Mon, 1=Tue, ..., 6=Sun) to your model's format
    week_lambda = (lambda x: 0 if x == 'Mon' else 1 if x == 'Tue' else 2 if x == 'Wed' else 3
                   if x == 'Thu' else 4 if x == 'Fri' else 5 if x == 'Sat' else 6)
    
    # If you need the exact weekday name (e.g., Mon, Tue, etc.), use this mapping
    weekday_map = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    arr_wd = arr_weekday  # Directly use the weekday number

    # Create input_data array to be passed to the model
    input_data = [[lt, mkt, spcl, price, adults, wknd, prk, wk, arr_day, arr_month, arr_wd]]

    if st.button('Predict'):
        response = prediction(input_data)
        st.success(response)

if __name__ == '__main__':
    main()
