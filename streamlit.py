import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache
def get_room_data(room_id):
    url = f'http://allisonhurley.com/api/journal/{room_id}'
    return pd.read_json(url)

@st.cache
def get_rooms:
    return pd.read_json('http://allisonhurley.com/api/rooms/')

'''
# Senior Design Counter

This is some _markdown_.

Go to [homepage](http://allisonhurley.com)
'''

rooms = get_rooms()
st.write(rooms)

df = get_room_data(1)
st.write('Test me', df)

#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)
#chart = st.line_chart(last_rows)

#for i in range(1, 101):
#    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#    status_text.text("%i%% Complete" % i)
#    chart.add_rows(new_rows)
#    progress_bar.progress(i)
#    last_rows = new_rows
#    time.sleep(0.05)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
#st.button("Re-run")

