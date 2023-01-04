import numpy as np
import pandas as pd

from utils import get_info

import streamlit as st

df = pd.read_csv('data/anime_list.csv')

#idx = df['English name'] == 'Unknown'
#df.loc[idx, 'English name'] = df.loc[idx, 'Name']

with st.sidebar:
    st.header('Select an Anime')
    option = st.selectbox('', df['English name'])

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