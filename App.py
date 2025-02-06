import streamlit as st 
import numpy as np 
import pandas as pd  
import pickle 
from xgboost import XGBClassifier

# Load the model
with open('Final_model_xgb.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction function
def prediction(input_data):
    input_data = np.array(input_data, dtype='object')
    pred = model.predict_proba(input_data)[:, 1][0]
    
    if pred > 0.5:
        return f'This Booking is more likely to get cancelled: Chances={round(pred * 100, 2)}%'
    else:
        return f'This Booking is less likely to get cancelled: Chances={round(pred * 100, 2)}%'

# Main function to render the Streamlit app
def main():
    # Title and header
    st.title('INN Hotels Booking Prediction')
    st.markdown("""
    Welcome to **INN Hotels** booking prediction model!  
    This model predicts the likelihood of a booking being canceled based on various inputs.
    Please provide the following details about the booking.
    """)
    
    # Banner image (you can add a hotel banner or related image here)
    st.image('hotel_banner.jpg', use_container_width=True)

    # Create a form layout for the input fields
    with st.form(key="booking_form"):
        # Lead Time (number input for better UX)
        lt = st.number_input('Lead time (in days)', min_value=0, step=1)
        
        # Type of Booking (selectbox)
        mkt = st.selectbox('Type of Booking', ['Online', 'Offline'], help="Choose whether the booking is made online or offline.")
        
        # Special Requests (dropdown to select the number of special requests)
        spcl = st.selectbox('Number of Special Requests', [0, 1, 2, 3, 4, 5], help="How many special requests have been made?")
        
        # Price of the room (number input for better UX)
        price = st.number_input('Price of the Room (in USD)', min_value=0.0, format="%.2f", help="Enter the price of the room.")

        # Number of Adults (selectbox)
        adults = st.selectbox('Number of Adults per Room', [1, 2, 3, 4], help="How many adults will stay in the room?")
        
        # Weekend Nights (number input)
        wknd = st.number_input('Number of Weekend Nights', min_value=0, step=1, help="How many weekend nights are booked?")
        
        # Parking Availability (selectbox with "Yes" or "No")
        prk = st.selectbox('Includes Parking Facility?', ['Yes', 'No'], help="Does the booking include parking?")
        
        # Weekday Nights (number input)
        wk = st.number_input('Number of Weekday Nights', min_value=0, step=1, help="How many weekday nights are booked?")
        
        # Arrival Date (Date picker for arrival date)
        arr_d = st.date_input('Arrival Date', help="Select the date of arrival.")
        
        # Extract Day, Month, and Weekday from arrival date
        arr_day = arr_d.day
        arr_month = arr_d.month
        arr_weekday = arr_d.weekday()  # Weekday (0 = Monday, 6 = Sunday)
        
        # Create the input data for the prediction model
        input_data = [[lt, 1 if mkt == 'Online' else 0, spcl, price, adults, wknd, 1 if prk == 'Yes' else 0, wk, arr_day, arr_month, arr_weekday]]

        # Submit Button
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Perform prediction
            response = prediction(input_data)
            st.success(response)

if __name__ == '__main__':
    main()
