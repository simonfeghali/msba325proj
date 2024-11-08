import streamlit as st

# Set the title of the Streamlit app
st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input("Enter the age you are expecting to live for:", min_value=1, step=1)

# Display the adjusted age and year if expected_age has been entered
if expected_age:
    adjusted_age = expected_age - 7
    st.write(f"NO, you will live {adjusted_age} years.")
