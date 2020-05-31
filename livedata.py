import time
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import pydeck as pdk

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
st.write(room_data)

room_layer = pdk.Layer('ColumnLayer', room_data, 
        get_position=['lon','lat'],
        get_elevation='count',
        radius=200,
        elevation_scale=100,
        elevation_range=[0,1000],
        pickable=True,
        auto_highlight=True,
        coverage=1,
        extruded=True)


st.pydeck_chart(pdk.Deck(
                 map_style="mapbox://styles/mapbox/light-v9",
                 initial_view_state={"latitude": 42.2738, "longitude": -83.4961, "zoom": 11, "pitch": 50},
                 layers=[room_layer],
              ))

def get_label(row):
    return room_data[room_data['id'] == row].iloc[0,1]

