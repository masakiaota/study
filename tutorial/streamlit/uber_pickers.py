# Tutorial: Create a data explorer app https://docs.streamlit.io/en/latest/tutorial/create_a_data_explorer_app.html

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Uber pickups in NYC')


st.subheader('Fetch some data')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')  # これで同じところにずっと文章を表示できるらしい
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')  # 自動的に書き換わるらしい 表示されることろは同じらしい
data_load_state.text("Done! (using st.cache)")

st.write(data.head())

st.subheader('Raw data')
'スクロールできるのも革命じゃん'
'基本的に`st.write`でおけ'
st.write(data)
'`st.dataframe`など専用の関数もある'
st.dataframe(data.head())


st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
'numpyでhistgramのデータ列を得るだけでok'
st.write(hist_values.reshape(1, -1))
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
'mapはあまり使わないので流しで'
st.map(data)  # 緯度経度を自動的に読み取ってるっぽい？


# hour_to_filter = 17
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)

st.subheader('Filter results with a slider')
# min: 0h, max: 23h, default: 17h
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


st.subheader('Use a button to toggle data')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
