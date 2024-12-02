import streamlit as st

st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input(
    "How long do you expect to live? Enter your guess to see what life in Lebanon might say about that!:",
    min_value=1, step=1
)

# Calculate only if the expected_age is at least 7 to avoid negative results
if expected_age >= 6:
    adjusted_age = expected_age - 5
    
    # Display the paragraph with the year in larger size
    st.markdown(
        f"""
        <p>Life in Lebanon had other plans…</p>
        <p>Your adjusted life expectancy is: 
        <span style="font-size: 48px; font-weight: bold;">{adjusted_age} years</span>.</p>
        <p>The challenges we are facing today are costing us more than we realize.</p>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Please enter an age of at least 6 to proceed with the calculation.")
