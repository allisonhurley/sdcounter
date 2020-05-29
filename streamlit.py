import time
import datetime
import numpy as np
import pandas as pd
import streamlit as st

@st.cache
def get_room_data(room_id,before,after):
    url = f'http://allisonhurley.com/api/journal/?before={before}&after={after}'
    if len(room_id) > 0:
       url = f'http://allisonhurley.com/api/journal/?rooms={room_id}&before={before}&after={after}'
    return pd.read_json(url)

@st.cache
def get_rooms():
    return pd.read_json('http://allisonhurley.com/api/rooms/')

'''
# Senior Design Counter

This is some _markdown_.

Go to [homepage](http://allisonhurley.com)
'''

room_data = get_rooms()
def get_label(row):
    return room_data[room_data['id'] == row].iloc[0,1]

start = st.date_input('Start Date', datetime.date(2020,1,1))
stop = st.date_input('Stop Date', datetime.datetime.now())

rooms = st.multiselect(
        "Select rooms", room_data['id'], format_func=get_label
)
rooms = '-'.join(map(str,rooms))
rooms = get_room_data(rooms,stop,start)

st.write(rooms)

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

