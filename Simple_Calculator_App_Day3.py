# ------------------------------------------------------------
# 💡 Project Name : Simple Calculator ➕➖✖️➗
# 🎯 Purpose      : Perform basic arithmetic operations with Streamlit (Enhanced UI)
# 👨‍💻 Developer   : Vision Vibes - Team 2 : S. Krishnakumar
# 🗓️ Context      : Gen-AI Python Training Daily Task
# ------------------------------------------------------------

import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# ------------------------------------------------------------
# 🧮 Function: Perform basic arithmetic operations
# ------------------------------------------------------------
def calculate(num1, num2, operation):
    """Performs the selected arithmetic operation."""
    if operation == "Addition (+)":
        return num1 + num2
    elif operation == "Subtraction (-)":
        return num1 - num2
    elif operation == "Multiplication (×)":
        return num1 * num2
    elif operation == "Division (÷)":
        if num2 == 0:
            return "⚠️ Cannot divide by zero!"
        return num1 / num2

# ------------------------------------------------------------
# 📄 Function: Generate PDF result
# ------------------------------------------------------------
def generate_pdf(num1, num2, operation, result):
    """Generates a PDF containing the calculation result."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 740, "Simple Calculator Report")

    c.setFont("Helvetica", 14)
    c.drawString(80, 690, f"Number 1      : {num1}")
    c.drawString(80, 660, f"Number 2      : {num2}")
    c.drawString(80, 630, f"Operation     : {operation}")
    c.drawString(80, 600, f"Result        : {result}")

    c.setFont("Helvetica-Oblique", 12)
    c.drawString(150, 550, "✅ Generated using Streamlit & Python (Gen-AI Training)")
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ------------------------------------------------------------
# 🌈 Streamlit Page Config & Custom CSS
# ------------------------------------------------------------
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.markdown(
    """
    <style>
    /* 🎨 Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #FCE38A, #F38181, #EAFFD0, #95E1D3);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* 🧮 Stylish Title */
    .title {
        text-align: center;
        color: #333333;
        font-size: 40px;
        font-weight: 900;
        text-shadow: 2px 2px #F8C8DC;
        margin-bottom: 10px;
    }

    /* 💫 Subtext */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #333;
        margin-bottom: 30px;
    }

    /* 🔘 Stylish Button */
    div.stButton > button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6em 1.5em;
        font-size: 18px;
        font-weight: 600;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #FFD93D;
        color: black;
        transform: scale(1.05);
    }

    /* 📥 Download Button */
    div.stDownloadButton > button {
        background-color: #6BCB77;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6em 1.5em;
        font-size: 18px;
        font-weight: 600;
        transition: 0.3s;
    }
    div.stDownloadButton > button:hover {
        background-color: #4D96FF;
        color: white;
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: gray;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# 🧮 Streamlit App UI
# ------------------------------------------------------------
st.markdown("<div class='title'>🧮 Simple Calculator Web App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>✨ Perform Quick & Accurate Calculations with Style ✨</div>", unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number:", step=1.0, format="%.2f")

with col2:
    num2 = st.number_input("Enter second number:", step=1.0, format="%.2f")

operation = st.selectbox(
    "Select Operation:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
)

# Button Action
if st.button("💫 Calculate Result"):
    result = calculate(num1, num2, operation)
    st.success(f"### ✅ Result: {result}")
    st.balloons()

    pdf_buffer = generate_pdf(num1, num2, operation, result)
    st.download_button(
        label="📥 Download Result as PDF",
        data=pdf_buffer,
        file_name="Calculator_Result.pdf",
        mime="application/pdf",
    )

# Footer
st.markdown("<div class='footer'>© 2025 Gen-AI Python Training | Developed by Vision Vibes - Team2</div>", unsafe_allow_html=True)
