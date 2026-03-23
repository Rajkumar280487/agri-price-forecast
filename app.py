import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Agricultural Price Forecast System")

# Load forecast data
data = pd.read_excel("forecast_30_days.xlsx")

st.subheader("30 Day Price Prediction")
st.dataframe(data)

st.subheader("Forecast Graph")

fig, ax = plt.subplots()
ax.plot(data["Date"], data["Predicted Price"])
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.set_title("30 Day Forecast")

st.pyplot(fig)