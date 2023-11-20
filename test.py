#house datatset#

import pandas as pd
import streamlit as st

house_df = pd.read_csv('hpi_edited-2.csv')
st.dataframe(house_df)

