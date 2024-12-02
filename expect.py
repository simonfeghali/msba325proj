import streamlit as st

# First Page
def main_page():
    st.title("Life Expectancy Predictor")
    
    # Prompt the user to enter their expected age
    expected_age = st.number_input(
        "How long do you expect to live? Enter your guess to see what life in Lebanon might say about that!:",
        min_value=1, step=1)
    
    # Button to navigate to the results page
    if st.button("Submit"):
        if expected_age >= 7:
            # Navigate to the second page with the input year as a parameter
            st.experimental_set_query_params(page="result", year=expected_age)
        else:
            st.warning("Please enter an age of at least 7 to proceed.")

# Second Page
def result_page():
    st.title("Life Expectancy Results")
    
    # Get the year parameter from the URL
    query_params = st.experimental_get_query_params()
    year = query_params.get("year", [""])[0]
    
    if year:
        # Display the year with a larger font size
        st.markdown(f"<h1 style='font-size: 50px;'>Your Expected Year: {year}</h1>", unsafe_allow_html=True)
        st.write(f"Life in Lebanon had other plans… Your adjusted life expectancy is: {int(year) - 7} years.")
        st.write("The challenges we are facing today are costing us more than we realize")
    else:
        st.error("No year found! Please go back and enter your expected age.")

# Main Logic
query_params = st.experimental_get_query_params()
if query_params.get("page", [""])[0] == "result":
    result_page()
else:
    main_page()
