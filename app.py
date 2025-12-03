import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")

st.write("Enter two numbers and choose an operation:")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First number", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("Second number", value=0.0, format="%.4f")

operation = st.selectbox(
    "Operation",
    ("Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)")
)

result = None
error_msg = ""

if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 == 0:
                error_msg = "Error: Division by zero is not allowed."
            else:
                result = num1 / num2
        elif operation == "Power (^)":
            result = num1 ** num2
    except Exception as e:
        error_msg = f"An error occurred: {e}"

if error_msg:
    st.error(error_msg)
elif result is not None:
    st.success(f"Result: {result}")
