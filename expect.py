# Set the title of the Streamlit app
st.title("Life Expectancy Predictor")

# Prompt the user to enter their expected age
expected_age = st.number_input("Enter the age you are expecting to live for:", min_value=0, step=1)

# When the user enters an age, display the adjusted age and year
if expected_age:
    adjusted_age = expected_age - 7
    current_year = datetime.now().year
    expected_year = current_year + adjusted_age
    st.write(f"NO, you will live {adjusted_age} years.")
