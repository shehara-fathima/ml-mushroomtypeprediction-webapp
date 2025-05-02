import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Mushroom type prediction app',
                   page_icon='🍄')
st.title("Is your mushroom edible or poisonous?")
st.write('This project aims promoting food safety by helping people identify toxic '
         'mushrooms, which reduces poisoning risks. It can support environmental conservation by monitoring species '
         'that signal ecosystem health, aiding biodiversity efforts.')


def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
def load_lottieur(url: str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding=load_lottiefile('/SHEHARA/Projects/ML/lotttie mushroom.json')

st_lottie(
    lottie_coding,
    speed=1,
    loop=True,
    width=500,
    height=400

)