import numpy as np
import pandas as pd

from utils import get_info

import streamlit as st

df = pd.read_csv('data/anime_list.csv')

with st.sidebar:
    st.header('Select an Anime')
    option = st.selectbox('', df['English name'])

    st.header('About')

    st.write("This is a the deployed content based anime recommendation system builty on myanimelist.net database available in [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020).")

    st.write("This web app is a part of Marcelo V. dos Santos data science portifolio.")

    st.write("Source code: https://github.com/mvsantosdev/anime_recommend")


st.header('Anime recommendation system')

info = df.set_index('English name').loc[option]

title = info.name.replace(':', ': ')

data = get_info(info.MAL_ID)

col1, col2 = st.columns([1, 2], gap='small')

col1.header(title)
col1.image(data['image'])

tab1, tab2 = col2.tabs(['Sinopse', 'Trailer'])

tab1.write(data['sinopse'])
tab2.video(data['teaser'])

dfw = pd.read_csv('models/weights.csv', index_col=0, header=[0, 1])
row = dfw.loc[info.MAL_ID]

idx = dfw.loc[info.MAL_ID].MAL_ID.values.astype(int)
weights = dfw.loc[info.MAL_ID].WEIGHT.values

size = 5

sim_idx = np.random.choice(idx, p=weights, size=size, replace=False)

st.header('Similar titles')

cols = st.columns(size)

for col, idx in zip(cols, sim_idx):
    sim = get_info(idx)
    col.image(sim['image'])

    name = df.set_index('MAL_ID').loc[idx, 'English name']
    col.write(f'{name}')