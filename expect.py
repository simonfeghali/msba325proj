import streamlit as st

st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input(
    "How long do you expect to live? Enter your guess (between 40 and 100):",
    min_value=40, max_value=100, step=1
)

# Display content only after the user enters a valid age
if expected_age > 0:  # Ensures the user has actively entered a value
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
    st.write("Enter your expected age to see the results.")
