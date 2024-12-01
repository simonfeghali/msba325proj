import streamlit as st

st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input("How long do you expect to live? Enter your guess to see what life in Lebanon might say about that!:", min_value=1, step=1)

# Calculate only if the expected_age is at least 7 to avoid negative results
if expected_age >= 7:
    adjusted_age = expected_age - 7
    st.write(f"Life in Lebanon had other plans… Your adjusted life expectancy is: {adjusted_age} years. The challenges we are facing today are costing us more than we realize")
else:
    st.write("Please enter an age of at least 7 to proceed with the calculation.")
