import streamlit as st

st.title("Life Expectancy Fun Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input("Enter the age you are expecting to live for:", min_value=1, step=1)

# Display the input to confirm it's working
st.write(f"You entered: {expected_age}")
