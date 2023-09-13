import streamlit as st

# Create a Streamlit app title
st.title("BMI Calculator")

# Create input fields for height and weight
height_cm = st.number_input("Enter your height (in centimeters)")
weight_kg = st.number_input("Enter your weight (in kilograms)")

# Convert height from cm to meters
height_m = height_cm / 100.0

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight_kg / (height_m ** 2)
    st.write(f"Your BMI is {bmi:.2f}")

    # Interpret BMI
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
