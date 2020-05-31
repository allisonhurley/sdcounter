import time
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import pydeck as pdk

def get_room_data(room_id,before,after):
    url = f'http://allisonhurley.com/api/journal/?before={before}&after={after}'
    if len(room_id) > 0:
       url = f'http://allisonhurley.com/api/journal/?rooms={room_id}&before={before}&after={after}'
    return pd.read_json(url)

def get_rooms():
    return pd.read_json('http://allisonhurley.com/api/rooms/')

'''
# Current Location Counts
'''

room_data = get_rooms()

room_layer = pdk.Layer('ColumnLayer', room_data, 
        get_position=['lon','lat'],
        get_elevation='count',
        get_fill_color=["count * 25"],
        radius=200,
        elevation_scale=100,
        elevation_range=[0,1000],
        pickable=True,
        auto_highlight=True,
        coverage=1,
        extruded=True)

tooltip = {
        "html": "<b>{name}</b>: <b>{count}</b>",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}


st.pydeck_chart(pdk.Deck(
                 map_style="mapbox://styles/mapbox/light-v9",
                 initial_view_state={"latitude": 42.2738, "longitude": -83.4961, "zoom": 11, "pitch": 50},
                 tooltip=tooltip, 
                 layers=[room_layer],
              ))

'''
&nbsp;

Table Data
'''

st.write(room_data)
