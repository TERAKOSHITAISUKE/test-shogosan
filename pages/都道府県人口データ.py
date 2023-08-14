import pandas as pd
import numpy as np
import streamlit as st

st.markdown(" # 都道府県人口データ ")

prefecture_list=['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県','石川県','福井県','山梨県',
'長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県']

selected_prefecture=st.selectbox (label="都道府県を選んでください",options=prefecture_list)

col_1,col_2=st.columns(2)
with col_1:
    df0=pd.read_csv('/Users/shogosoma/Desktop/０からはじめるPandas/pandas_lecture/data/population.csv',encoding='shift-jis',index_col=1)
    df0=df0.loc[:,["西暦（年）","人口（男）","人口（女）","人口（総数）"]]
    df0=df0.loc[[ '北海道','青森県','岩手県','宮城県',         '秋田県',         '山形県',         '福島県',
                '茨城県',         '栃木県',         '群馬県',         '埼玉県',
                '千葉県',         '東京都',        '神奈川県',         '新潟県',
                '富山県',         '石川県',         '福井県',         '山梨県',
                '長野県',         '岐阜県',         '静岡県',         '愛知県',
                '三重県',         '滋賀県',         '京都府',         '大阪府',
                '兵庫県',         '奈良県',        '和歌山県',         '鳥取県',
                '島根県',         '岡山県',         '広島県',         '山口県',
                '徳島県',         '香川県',         '愛媛県',         '高知県',
                '福岡県',         '佐賀県',         '長崎県',         '熊本県',
                '大分県',         '宮崎県',        '鹿児島県',         '沖縄県'],:]
    df0['人口（男）'] = pd.to_numeric(df0['人口（男）'], errors='coerce')
    df0['人口（女）'] = pd.to_numeric(df0['人口（女）'], errors='coerce')
    df0=df0.dropna()
    df0['人口（男）'] = df0['人口（男）'].astype(int)
    df0['人口（女）'] = df0['人口（女）'].astype(int)
    df0['西暦（年）'] = df0['西暦（年）'].astype(int)
    df0['人口（総数）'] = df0['人口（総数）'].astype(int)
    df1=df0.loc[selected_prefecture,:]
    df1
with col_2:

    df1.set_index('西暦（年）',inplace=True)
    data=df1[["人口（総数）"]]

    st.bar_chart(data)

df2=df1.loc[:,["人口（男）","人口（女）"]]
data2=df2
st.bar_chart(data2)