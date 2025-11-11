# ------------------------------------------------------------
# 🧠 Project : Greeting Form App
# 🎯 Purpose : Take user name & age, then show a personalized greeting
# 👨‍💻 Developer : S.Krishnakumar
# ------------------------------------------------------------

# 📦 Import the required Streamlit library
import streamlit as st

# 🏷️ App Title
st.set_page_config(page_title="Welcome App", page_icon="✨")
st.title("✨ Welcome to the GenAI Training Portal ✨")
st.subheader("Let's create your personalized greeting below 👇")

# ------------------------------------------------------------
# 🧾 FORM SECTION
# Using 'with st.form' lets us control when the form submits
# ------------------------------------------------------------
with st.form("greeting_form"):
    # 🧍 Name Input
    name = st.text_input("Enter your name:")

    # 🎚️ Age Input (slider)
    age = st.slider("Select your age:", min_value=10, max_value=100, value=25)

    # 🪄 Submit Button
    submit_button = st.form_submit_button(label="Show Greeting")

# ------------------------------------------------------------
# 💬 OUTPUT SECTION
# Display greeting only when the form is submitted
# ------------------------------------------------------------
if submit_button:
    if name.strip() == "":
        st.warning("⚠️ Please enter your name to continue!")
    else:
        # Create a positive and warm greeting message
        st.success(f"🎉 Hi {name}! You're {age} years young and full of energy!")
        st.balloons()  # Fun animation!

        # Additional motivational quote
        st.markdown(
            f"""
            🌟 **Keep learning and shining, {name}!**
            <br>Every day in GenAI training is a step toward innovation 🚀
            """,
            unsafe_allow_html=True
        )

# ------------------------------------------------------------
# 📘 End of App
# ------------------------------------------------------------
