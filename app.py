import streamlit as st
import pandas as pd
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...

pickup_date = st.date_input('Pickup Date')
pickup_time = st.time_input('Pickup Time',)
pickup_longitude = st.number_input('Pickup Longitude', )
pickup_latitude = st.number_input('Pickup Latitude', )
dropoff_longitude = st.number_input('Dropoff Longitude',)
dropoff_latitude = st.number_input('Dropoff Latitude', )
passenger_count = st.number_input('Passenger Count', )


predict = {
    "pickup_datetime" : str(pickup_date)+' '+str(pickup_time),
    'pickup_longitude': float(pickup_longitude),
    'pickup_latitude': float(pickup_latitude),
    'dropoff_longitude': float(dropoff_longitude),
    'dropoff_latitude': float(dropoff_latitude),
    'passenger_count': int(passenger_count)
}

if st.button('Predict'):
    # 3. Let's call our API using the requests package...
    response = requests.get(url, params=predict)

    # 4. Let's retrieve the prediction from the JSON returned by the API...
    prediction = response.json()

    # Finally, we can display the prediction to the user
    st.write('Prediction:', prediction)
