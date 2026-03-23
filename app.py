import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Black Gram Price Forecast - Guntur")

st.title("Black Gram Price Forecast - Venigandla, Guntur")
st.subheader("మినుములు (Black Gram)")

# load dataset
data = pd.read_excel("cleaned_agri_price_2024_2025_FIXED.xlsx")
data['Price Date'] = pd.to_datetime(data['Price Date'])

# simulate live price
base_price = data['Modal Price'].iloc[-1]
live_price = base_price + np.random.normal(0, 20)

# buy sell signal
if live_price > base_price:
    signal = "BUY ▲"
    color = "🟢"
else:
    signal = "SELL ▼"
    color = "🔴"

# top dashboard
col1, col2, col3 = st.columns(3)

col1.metric("Crop", "Black Gram")
col2.metric("Live Price (₹)", f"{live_price:.2f}")
col3.metric("Location", "Guntur")

st.write(f"### Signal: {color} {signal}")

# LIVE MARKET CHART (dark theme)
st.subheader("Live Market Chart")

live_prices = []
timestamps = []

current = live_price

for i in range(30):
    current += np.random.normal(0, 10)
    live_prices.append(current)
    timestamps.append(i)

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(timestamps, live_prices, color='red', linewidth=2)

ax.set_facecolor("black")
fig.patch.set_facecolor("black")

ax.set_title("Live Black Gram Market", color="white")
ax.set_xlabel("Time", color="white")
ax.set_ylabel("Price", color="white")

st.pyplot(fig)

# forecast
window = 7
data['MA'] = data['Modal Price'].rolling(window).mean()

last_price = data['MA'].iloc[-1]

future_days = 30
future_dates = pd.date_range(
    start=data['Price Date'].iloc[-1],
    periods=future_days
)

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

plt.style.use('dark_background')

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(data['Price Date'], data['Modal Price'], label='Actual', color='white')
ax2.plot(future_dates, predictions, label='Forecast', color='red')

ax2.legend()
ax2.set_facecolor("black")
fig2.patch.set_facecolor("black")

st.pyplot(fig2)
