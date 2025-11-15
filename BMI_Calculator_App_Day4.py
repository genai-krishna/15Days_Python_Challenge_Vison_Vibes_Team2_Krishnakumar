import streamlit as st
from fpdf import FPDF

# ----------------------------
# APP CONFIG
# ----------------------------
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="centered"
)

# ----------------------------
# HELPER: Calculate BMI
# ----------------------------
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# ----------------------------
# HELPER: Determine BMI Category
# ----------------------------
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🔵"
    elif 18.5 <= bmi <= 24.9:
        return "Normal", "🟢"
    elif 25 <= bmi <= 29.9:
        return "Overweight", "🟡"
    else:
        return "Obese", "🔴"

# ----------------------------
# PDF GENERATION
# ----------------------------
def generate_pdf(name, height, weight, bmi, category):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="BMI REPORT", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(100, 10, txt=f"Height: {height} cm", ln=True)
    pdf.cell(100, 10, txt=f"Weight: {weight} kg", ln=True)
    pdf.cell(100, 10, txt=f"BMI: {bmi}", ln=True)
    pdf.cell(100, 10, txt=f"Category: {category}", ln=True)

    file_path = "bmi_report.pdf"
    pdf.output(file_path)
    return file_path

# ----------------------------
# MAIN UI
# ----------------------------
st.title("🧮 BMI Calculator")
st.write("### A simple & professional BMI calculator built with Streamlit")

with st.container():
    st.markdown("#### Enter Your Details")

    name = st.text_input("Your Name")
    height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, step=1)

# Once user clicks button
if st.button("Calculate BMI"):
    if height and weight:
        bmi = calculate_bmi(height, weight)
        category, icon = bmi_category(bmi)

        st.success(f"**Your BMI is: {bmi}**")
        st.info(f"**Category:** {category} {icon}")

        # Display result card
        with st.container():
            st.markdown("---")
            st.subheader("📄 Your BMI Summary")
            st.write(f"**Name:** {name}")
            st.write(f"**Height:** {height} cm")
            st.write(f"**Weight:** {weight} kg")
            st.write(f"**BMI:** {bmi}")
            st.write(f"**Category:** {category} {icon}")
            st.markdown("---")

        # PDF Download
        file_path = generate_pdf(name, height, weight, bmi, category)

        with open(file_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Download BMI Report (PDF)",
                data=pdf_file,
                file_name="BMI_Report.pdf",
                mime="application/pdf"
            )

    else:
        st.error("Please enter valid height and weight.")

# FOOTER
st.markdown(
    """
    <hr>
    <center>
    <p style='color:gray;'>Created for Gen-AI Training • Professional BMI App</p>
    </center>
    """,
    unsafe_allow_html=True
)
