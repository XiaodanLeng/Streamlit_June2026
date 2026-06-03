import streamlit as st
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')

# step 8
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')



#Step 8
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Step 9

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# Step 12
#place @st.cache_data in front of the load_data function
# to save the raw data into temperary storage

# Step 13: Replace the argument "Loading data...done!" 
# in data_load_state_text with that in the following
# "Done! (using st.cache_data)"

# Step 16: look at the data source, rerun the app


#st.subheader('Raw data')
#st.write(data)

# wrapt the above with an if statement
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

# Step 18 Draw histogram

# add a check box later
if st.checkbox("Show histogram"):
    st.subheader('Number of pickups by hour')

    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

    st.bar_chart(hist_values)

# Step 20 add a map
#st.subheader('Map of all pickups')

#st.map(data)

# Step 22 focus on the hour of 17:00
#hour_to_filter = 17
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')

#st.map(filtered_data)

# Step 24  made more detailed filter by adding a slider
# add a checkbox
if st.checkbox("Show map"):

    hour_to_filter = st.slider('hour', 0, 23, 17)
    # min: 0h, max: 23h, default: 17h
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)

# Step 26 Add a checkbox for controlling the raw data display option
# wrapt the follow lines

#st.subheader("Raw data")
#st.write(data)

# by an if statement

#if st.checkbox("Show raw data"):
#    st.subheader("Raw data")
#    st.write(data)
# add a wraper for bar chart for histogram


