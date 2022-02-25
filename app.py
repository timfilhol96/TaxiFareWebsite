from tkinter import Image
import streamlit as st
import requests
from PIL import Image
import datetime
import pandas as pd

'''
# 🚕 NY Taxi fare calculator 🚕
'''

st.markdown('''
### 🤓 Please enter the following info 🤓:

''')
columns = st.columns(2)
date = columns[0].date_input("📅 Select a date 📅",datetime.date(2022, 2, 25))
time = columns[1].time_input('⏱️ Select a time ⏱️',datetime.time(11, 45))

columns = st.columns(2)
pickup_longitude=columns[0].number_input('Pickup Longitude',40.7614327)
pickup_latitude=columns[1].number_input('Pickup Latitude',-73.9798156)

columns = st.columns(2)
dropoff_longitude=columns[0].number_input('Dropoff Longitude',40.6513111)
dropoff_latitude=columns[1].number_input('Dropoff Latitude',-73.8803331)

passenger_count=st.slider('🕺 Passenger Count 🕺', 1, 4, 1)

url = 'https://taxifare.lewagon.ai/predict'

params={'pickup_datetime': f"{str(date)} {str(time)}",
'pickup_longitude': pickup_longitude,
'pickup_latitude': pickup_latitude,
'dropoff_longitude': dropoff_longitude,
'dropoff_latitude': dropoff_latitude,
'passenger_count': passenger_count
    }

df=pd.DataFrame([[pickup_longitude,pickup_latitude],[dropoff_longitude,dropoff_latitude]],columns=['lat','lon'])

st.map(df)

response= requests.get(
    url,
    params,
).json()


if st.button('Get the fare 💵'):
    st.metric('Predicted Fare',f'{round(response["fare"],2)} USD')
    st.markdown("![Alt Text](https://media1.giphy.com/media/14SAx6S02Io1ThOlOY/giphy.gif?cid=ecf05e47bqzrw6oixl94iiis8dlaor7pnduytptyuecy9ud1&rid=giphy.gif)")
