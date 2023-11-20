#house datatset#

import pandas as pd
import streamlit as st
import altair as alt

house_df = pd.read_csv('hpi_edited-2.csv')
st.dataframe(house_df)

scatter = alt.Chart(house_df, title='My new chart title').mark_point(size=100, opacity= .9, fill='green', color='green').encode(
    alt.X('grade of the house',title= 'grade'),
    alt.Y('Area of the house(excluding basement)',title= 'Area')
)
st.altair_chart(scatter, use_container_width=True)


