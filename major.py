import streamlit as st

# Define function to calculate BMI
def calculate_bmi(height, weight):
    bmi = weight / (height/100)**2
    return round(bmi, 2)

# Define Streamlit app
def app():
    # Set page title and description
    st.title("BMI Calculator")
    st.write("Enter your details below to calculate your BMI.")

    # Define input fields
    name = st.text_input("Name")
    gender = st.radio("Gender", ("Male", "Female", "Other"))
    age = st.number_input("Age", min_value=1, max_value=150, step=1)
    address = st.text_area("Address")
    hobbies = st.multiselect("Hobbies", ["Reading", "Sports", "Traveling", "Music"])
    weight = st.number_input("Weight (in kg)", min_value=1, max_value=1000, step=1)
    height = st.number_input("Height (in cm)", min_value=1, max_value=300, step=1)

    # Calculate BMI and display result
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight)
        st.write(f"Hello {name}, your BMI is {bmi}.")

if __name__ == '__main__':
    app()
