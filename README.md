# Hotel Inn - AI-Powered Booking Cancellation Predictor 🏨

![Banner](<img width="530" alt="Image" src="https://github.com/user-attachments/assets/8719081d-5440-4a0b-8609-93b4d126af35" />)

Hotel Inn is an AI-powered Streamlit application designed to predict the likelihood of booking cancellations. The app uses a machine learning model to assess booking details and predict the chances of cancellation based on various features like lead time, booking type, special requests, and more.

## **Features**

- **Cancellation Prediction:** Enter booking details to get an AI-powered prediction on the likelihood of cancellation.
- **Interactive Interface:** Built with Streamlit, the app allows users to enter booking-related information via text inputs, dropdowns, and date pickers.
- **Machine Learning Model:** The prediction is powered by an XGBoost model that has been trained on historical booking data to forecast cancellation chances.

---

## **How to Use**

1. **Enter Booking Information:**
    - Fill out the booking details such as **Lead Time**, **Booking Type** (Online or Offline), **Special Requests**, **Room Price**, **Number of Adults**, **Weekend Nights**, **Parking Availability**, **Weekday Nights**, and the **Date of Arrival**.
    - Use the **Date Picker** to select the arrival date.

2. **Get Cancellation Prediction:**
    - Click the **Predict** button after entering the details.
    - The app will provide a prediction on whether the booking is likely to be canceled, along with the probability in percentage.

---

## **Technical Stack**

- **Streamlit:** For building the interactive web-based application.
- **XGBoost:** Machine learning model used for predicting booking cancellations.
- **Pandas & NumPy:** For data manipulation and handling.
- **Pickle:** To load and use the pre-trained XGBoost model.

---

## **Installation**

To run the **Hotel Inn** app locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/hotel-inn.git
   cd hotel-inn
