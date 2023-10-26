
import streamlit as st

st.header('This video is brought to you by baba Aamar')
st.text('are you enjoying learning?')

st.header('what do you want to write?')

import seaborn as sns
df = sns.load_dataset('iris')
st.write(df[['species','sepal length','petal_length']].head(10))

st.bar_chart(df['sepal_length'])

st.line_chart(df['sepal_length'])

