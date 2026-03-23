st.markdown(
    """
    <meta name="google-site-verification" content="<meta name="google-site-verification" content="Or_SUTi4xFVO3p6NTW-uphsYbHA-G6BkgNnOnwufk8o" />" />
    """,
    unsafe_allow_html=True
)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Agricultural Price Forecast System")

st.title("Real-Time Agricultural Price Forecast System")

# Load historical data
data = pd.read_excel("cleaned_agri_price_2024_2025_FIXED.xlsx")

data['Price Date'] = pd.to_datetime(data['Price Date'])

# Add today's date automatically (live update)
today = pd.Timestamp.today().normalize()

latest_price = data['Modal Price'].iloc[-1]

today_row = pd.DataFrame({
    "Price Date": [today],
    "Modal Price": [latest_price]
})

data = pd.concat([data, today_row], ignore_index=True)

# Train ML model
X = np.arange(len(data)).reshape(-1,1)
y = data['Modal Price']

model = LinearRegression()
model.fit(X,y)

# Predict next 30 days
future_days = 30

future_X = np.arange(len(data), len(data)+future_days).reshape(-1,1)
predictions = model.predict(future_X)

future_dates = pd.date_range(
    start=today,
    periods=future_days,
    freq='D'
)

forecast = pd.DataFrame({
    "Date": future_dates.strftime('%Y-%m-%d'),
    "Predicted Price": predictions
})

st.subheader("30 Day Price Prediction")
st.dataframe(forecast)

st.subheader("Forecast Graph")

plt.figure(figsize=(12,5))

plt.plot(data['Price Date'], data['Modal Price'], label='Actual Price')
plt.plot(future_dates, predictions, label='Forecast Price')

plt.legend()
plt.xticks(rotation=45)

st.pyplot(plt)
