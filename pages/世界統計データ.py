import pandas as pd
import numpy as np
import os
import streamlit as st

data_set=px.data.gapminder()
years_list=list(data_set["year"].unique())
country_list=list(data_set["country"].unique())

selected_country=st.multiselect(label="表示する国名を選択してください。複数選択可能。",options=country_list,default=["Japan","United States"])
selected_year=st.selectbox(label="表示する年を選択してください。", options=years_list)

df=pd.DataFrame()
for country in selected_country:
    new_data=data_set[data_set["country"]==country]
    df=pd.concat([df,new_data])
    
df_show=df[df["year"]==selected_year]
df_show=df_show.loc[:,["country","lifeExp","pop","gdpPercap"]]

df_show

st.write("人口")
chart_data1 = df_show.loc[:,["country","pop"]]
chart_data1.set_index("country", inplace=True)
st.bar_chart(chart_data1)

st.write("一人当たりGDP")
chart_data2 = df_show.loc[:,["country","gdpPercap"]]
chart_data2.set_index("country", inplace=True)
st.bar_chart(chart_data2)

st.write("平均寿命")
chart_data3 = df_show.loc[:,["country","lifeExp"]]
chart_data3.set_index("country", inplace=True)
y_min = 40
y_max = 90
st.bar_chart(chart_data3,use_container_width=True)