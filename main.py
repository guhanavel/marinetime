import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from PIL import Image
import streamlit.components.v1 as components


start = st.sidebar.selectbox(
    "Enter your Start Location",
    ("","Singapore",))

end = st.sidebar.selectbox(
    "Enter your Destination",
    ("","Nhava Sheva",))

search = st.sidebar.button(label="Search")



air_route = st.sidebar.container()


cods = [
    ['Singapore', 1.28967,103.85007],
    ['Nhava Sheva',18.949935913085938,72.95118713378906],
    ['Port Klang', 3.0186,101.4286],
    ['Kattupalli', 13.3120155,80.3450866],
    ['Colombo ',6.927079, 79.861244]]

df = pd.DataFrame(
    cods,
    columns=['Name','lat', 'lon'])
HtmlFile_2 = open("SY.html", 'r', encoding='utf-8')
source_code_2 = HtmlFile_2.read()
a = components.html(source_code_2,height=500,width=900)

HtmlFile = open("iframe.html", 'r', encoding='utf-8')
source_code_1 = HtmlFile.read()

if search:
    a.empty()
    components.html(source_code_1,height=500,width=900)
    best = Image.open('Mix.png')
    st.sidebar.image(best)
    best_2 = Image.open('Mix2.png')
    sea = Image.open('Sea.png')
    st.sidebar.image(sea)
    st.sidebar.image(best_2)
    air = Image.open('Air.png')
    st.sidebar.image(air)
