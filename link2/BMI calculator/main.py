import streamlit as st

st.title("BMI CALCULSTOR")

weight = st.number_input("Enter your weight in kg")

height = st.number_input("Enter your height in cm")

final_height = height ** 2

if st.button("Calculate BMI"):
    bmi = weight/final_height
    st.success(f'your BMI is: {bmi :2f}')

    if bmi<18.5:
        st.warning("Your are under weight")
    elif 18.5 >= bmi < 24.9:
        st.info("You have a normal weight")
    elif 25 <= bmi <29.5:
        st.warning("You are over weight")
    else:
        st.error("You are obese.")