## 🌦️ Features
This project is a user-friendly web app for displaying accurate weather forecasts based on your location. Built with Python, it uses streamlit for the interface, open-meteo for weather data, and pandas and matplotlib for data processing and visualization. 🌞🌧️❄️

## 🧰 Features
- Location-Based Forecasts: Enter your city, country, postal code, and state (for the US) to get real-time weather data.

- Temperature Charts: Visualize hourly temperature trends over the selected number of days using matplotlib.

- Current Weather Analysis: Get a personalized description of the weather with matching icons based on temperature ranges.
  
- Interactive Interface: Powered by streamlit, you can select the number of forecast days, interact with sliders,the location you want to see the weather for and get instant weather insights.

## 📝 Code Overview
Weather Class: This is where data is fetched, processed, and prepared for display. Key methods:
 - get_response(): Connects to the API and retrieves weather data.
 - get_Long_Lat(): Uses API to fetch the latitude and longitude corrosponding to your location.
 - get_temp(): Uses pandas to organize temperature data by day for plotting.
 - current_Temp(): Retrieves the current temperature.
 - display_weather_analysis(): Uses temperature thresholds to generate a description and icon for current weather.
 - graph_it(): Plots temperature vs. time using matplotlib for each day.
Streamlit Web Interface:
 - create_webpage(): Sets up user inputs and UI elements in Streamlit.
 - main(): Manages the app flow, calling relevant methods to fetch and display data.

