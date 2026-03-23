import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Black Gram Price Forecast - Guntur")

st.title("Black Gram Price Forecast - Venigandla, Guntur")
st.subheader("మినుములు (Black Gram)")

# load dataset
data = pd.read_excel("cleaned_agri_price_2024_2025_FIXED.xlsx")
data['Price Date'] = pd.to_datetime(data['Price Date'])

# simulate live price
base_price = data['Modal Price'].iloc[-1]
live_price = base_price + np.random.normal(0, 20)

# recommendation logic
if live_price > base_price:
    recommendation = "SELL"
    color = "🟢"
else:
    recommendation = "HOLD"
    color = "🟡"

# current price box
col1, col2, col3 = st.columns(3)

col1.metric("Crop", "Black Gram")
col2.metric("Live Price (₹)", f"{live_price:.2f}")
col3.metric("Location", "Guntur")

st.write(f"### Recommendation: {color} {recommendation}")

# LIVE MARKET CHART (Trading style)
st.subheader("Live Market Chart")

live_prices = []
timestamps = []

current = live_price

for i in range(30):
    current += np.random.normal(0, 10)
    live_prices.append(current)
    timestamps.append(i)

fig, ax = plt.subplots()
ax.plot(timestamps, live_prices)
ax.set_xlabel("Time")
ax.set_ylabel("Price")

st.pyplot(fig)

# forecast model
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

st.subheader("30 Day Forecast")
st.dataframe(forecast)

st.subheader("Forecast Graph")

plt.figure(figsize=(12,5))
plt.plot(data['Price Date'], data['Modal Price'], label='Actual')
plt.plot(future_dates, predictions, label='Forecast')

plt.legend()
plt.xticks(rotation=45)

st.pyplot(plt)
