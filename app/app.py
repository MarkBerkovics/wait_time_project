import streamlit as st
import requests
import matplotlib.image as mpimg

st.markdown("# Customer service wait time calculator")
st.markdown("### Just enter the day of the week and the time of the day and click the button")
st.markdown("")

day = st.number_input("Enter a day of the week", min_value=1, max_value=7)
time = st.number_input("Enter a time of the day", min_value=1, max_value=24)

url = "https://image-of-my-app-v7n7mb57hq-ew.a.run.app/predict"
params = {
    "day_of_week": day,
    "time_of_day": time
}

response = requests.get(url, params).json()
waiting = response['Minutes to wait']

if st.button("Calculate"):
    st.write(f"Your wait time is {waiting} minutes")
    st.image(mpimg.imread("raw_data/upset-person-on-phone-760.jpg"))
