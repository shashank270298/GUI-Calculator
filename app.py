import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")


dark_theme = """
    <style>
    html, body, [class*="stApp"] {
        background-color: #0E1117 !important;
        color: #D1D5DB !important;  /* Force gray text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #E5E7EB !important;
    }

    p, span, label, div, .css-1cpxqw2, .css-1d391kg {
        color: #D1D5DB !important;
    }

    .css-1d391kg {
        background-color: #161A23 !important;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.4);
    }

    /* Button styling */
    .stButton>button {
        background-color: #1F2937 !important;
        color: #FAFAFA !important;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        box-shadow: 0px 3px 5px rgba(0,0,0,0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        transform: scale(1.05);
    }

    /* Radio button labels */
    .stRadio>div>label {
        background-color: #1F2937 !important;
        padding: 8px 14px;
        border-radius: 8px;
        color: #D1D5DB !important;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }
    .stRadio>div>label:hover {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
    }

    /* Input fields */
    .stNumberInput input, .stTextInput input {
        background-color: #1F2937 !important;
        color: #D1D5DB !important;
        border-radius: 6px;
        padding: 6px;
        border: 1px solid #374151;
    }
    </style>
"""

st.markdown(dark_theme, unsafe_allow_html=True)

st.title("🧮 Calculator — Dark Theme")
st.write("A modern, minimal calculator built with **Python** & **Streamlit**")

def clear_all():
    st.session_state.num1 = 0.0
    st.session_state.num2 = 0.0
    st.session_state.result = ""

num1 = st.number_input("Enter First Number", value=0.0, step=1.0, key="num1")
a = st.session_state.num1

num2 = st.number_input("Enter Second Number", value=0.0, step=1.0, key="num2")
b= st.session_state.num2

operation = st.radio("Select Operation",["➕ Addition","➖ Subtraction","✖ Multiplication","➗ Division"], horizontal=True, key="operation")
op = st.session_state.operation

col1, col2 = st.columns([1, 1])

# Initialize session state for result
if "result" not in st.session_state:
   st.session_state.result = ""

# Calculate Button
with col1:
    if st.button("Calculate"):
        try:
            if op == "➕ Addition":
                st.session_state.result = a+b
            elif op == "➖ Subtraction":
                st.session_state.result = a-b
            elif op == "✖ Multiplication":
                st.session_state.result = a*b
            elif op == "➗ Division":
                if num2 == 0:
                    st.error("🚨 Cannot divide by zero!")
                    st.session_state.result = ""
                else:
                    st.session_state.result = a/b
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Clear Button
with col2:
    st.button("Clear", on_click=clear_all)

# Display result
if st.session_state.result != "":
    st.success(f"**Result:** {st.session_state.result}")
        
st.markdown("---")
st.caption(
    "<p style='text-align: center; color: gray;'>© 2025 • Designed by <b>Shashank Sharma</b></p>",
    unsafe_allow_html=True
)