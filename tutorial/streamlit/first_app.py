# https://docs.streamlit.io/en/latest/getting_started.html こちらのtutorial

import streamlit as st
# # To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')

st.write('unko すげええええええ')
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)
df  # st.writeは省略できるっぽい？


'あとでこれも見ておいたほうが良さそう https://docs.streamlit.io/en/latest/tutorial/create_a_data_explorer_app.html'


'''
そのまま書き込めるの神じゃん
'''
3

2

3 + 2  # 数字も全部行ける

'## Draw a line chart'

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'## Plot a map'
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
