import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Agricultural Price Forecast System")

st.title("Agricultural Price Forecast System")

# load dataset
data = pd.read_excel("cleaned_agri_price_2024_2025_FIXED.xlsx")

data['Price Date'] = pd.to_datetime(data['Price Date'])

# train ML model
X = np.arange(len(data)).reshape(-1,1)
y = data['Modal Price']

model = LinearRegression()
model.fit(X,y)

# predict from TODAY
future_days = 30

future_X = np.arange(len(data), len(data)+future_days).reshape(-1,1)
predictions = model.predict(future_X)

today = pd.Timestamp.today().normalize()

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
plt.plot(future_dates, predictions, label='Forecast Price', color='orange')

plt.legend()
plt.xticks(rotation=45)

st.pyplot(plt)
