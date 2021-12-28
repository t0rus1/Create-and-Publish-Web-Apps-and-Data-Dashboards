import streamlit as st
import pandas as pd

data = {
  'Series_1': [1,3,2,4,8,5],
  'Series_2': [12,33,12,74,38,55]
}

df = pd.DataFrame(data)


st.title('Our first Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our 
first Web App
Enjoy it
''')

st.write(df)
st.line_chart(df)