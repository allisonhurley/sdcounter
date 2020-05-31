import time
import datetime
import plotly.express as px
from datetime import timedelta
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

def get_room_data(room_id,before,after):
    url = f'http://allisonhurley.com/api/journal/?before={before}&after={after}'
    if len(room_id) > 0:
       url = f'http://allisonhurley.com/api/journal/?rooms={room_id}&before={before}&after={after}'
    return pd.read_json(url)

def get_rooms():
    return pd.read_json('http://allisonhurley.com/api/rooms/')

'''
# Count History

'''

room_data = get_rooms()
def get_label(row):
    return room_data[room_data['id'] == row].iloc[0,1]

start = st.date_input('Start Date', datetime.date(2020,1,1))
stop = st.date_input('Stop Date', datetime.datetime.now()) + timedelta(days=1)

rooms = st.multiselect(
        "Select rooms", room_data['id'], format_func=get_label
)
color_type = 'delta' if len(rooms) == 1 else 'room_id'
rooms = '-'.join(map(str,rooms))
rooms = get_room_data(rooms,stop,start)

rooms['binned_hours'] = rooms['applied_at'].dt.hour


hist_data = rooms.groupby(['binned_hours','room_id']).agg('mean')
hist_data = hist_data.reset_index()
fig = px.bar(hist_data,x='binned_hours',y='count',color='room_id')
st.plotly_chart(fig)
st.write(hist_data)

