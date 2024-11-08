import streamlit as st

st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input("Enter the age you are expecting to live for:", min_value=1, step=1)

# Calculate only if the expected_age is at least 7 to avoid negative results
if expected_age >= 7:
    adjusted_age = expected_age - 7
    st.write(f"NO, you will live {adjusted_age} years.")
else:
    st.write("Please enter an age of at least 7 to proceed with the calculation.")
