import streamlit as st
import requests
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Air Quality Prediction App")
lat = st.number_input("Latitude", value= 28.6139)
lon = st.number_input("Longitude", value= 77.2090)

if st.button("Get AQI"):
    API_KEY = '44d70dd7deb08333e61ac981f618908f'
    lat, lon = 28.6139, 77.2090 ## Delhi Co-ordinates
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    aqi = data['list'][0]['main']['aqi']
    st.write(f'Air Quality Index (AQI): {aqi}')
    ## Simulated sample Data
    X = np.array([[10], [20], [30], [40], [50]])  ## Tempreture
    y = np.array([80, 70, 60, 50, 40])  ##AQI

    model = LinearRegression()
    model.fit(X,y)
    prediction = model.predict([[35]])
    st.write(f'Predicted AQI (for demo): {prediction[0]:.2f}')
