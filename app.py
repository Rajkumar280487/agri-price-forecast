import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Black Gram Price Forecast - Guntur")

st.title("Black Gram Price Forecast - Venigandla, Guntur")

st.write("Real-time price prediction for Black Gram using historical market data.")

# load dataset
data = pd.read_excel("cleaned_agri_price_2024_2025_FIXED.xlsx")

data['Price Date'] = pd.to_datetime(data['Price Date'])

# moving average forecast
window = 7
data['MA'] = data['Modal Price'].rolling(window).mean()

last_price = data['MA'].iloc[-1]

future_days = 30
future_dates = pd.date_range(start=pd.Timestamp.today(), periods=future_days)

predictions = []

current = last_price

for i in range(future_days):
    noise = np.random.normal(0, 50)
    current = current + noise
    predictions.append(current)

forecast = pd.DataFrame({
    "Date": future_dates.strftime('%Y-%m-%d'),
    "Predicted Price": predictions
})

st.subheader("30 Day Black Gram Price Prediction")
st.dataframe(forecast)

st.subheader("Forecast Graph")

plt.figure(figsize=(12,5))
plt.plot(data['Price Date'], data['Modal Price'], label='Actual')
plt.plot(future_dates, predictions, label='Forecast')

plt.legend()
plt.xticks(rotation=45)

st.pyplot(plt)
