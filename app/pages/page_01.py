import streamlit as st

st.markdown("This is page 1")
st.markdown("This is my secret:")
secret = st.secrets['MY_SECRET']
st.write(secret)
