# ------------------------------------------------------------
# 💡 Project Name : Friends Expense Splitter (Streamlit App)
# 🎯 Purpose      : Split total expenses among friends fairly
# 👨‍💻 Developer   : Vision_Vibes_Team2: S.Krishnakumar
# 🗓️ Context      : Gen-AI Python Training (Daily Task)
# ------------------------------------------------------------
# 📦 Requirements : streamlit (install via `pip install streamlit`)
# ------------------------------------------------------------

import streamlit as st

# 🎨 Page setup
st.set_page_config(
    page_title="Friends Expense Splitter 💰",
    page_icon="💸",
    layout="centered"
)

# ------------------------------------------------------------
# 🏷️ HEADER SECTION
# ------------------------------------------------------------
st.markdown(
    """
    <div style='text-align:center'>
        <h1>💰 Friends Expense Splitter</h1>
        <h4>✨ Split bills easily, fairly, and transparently!</h4>
        <p style='color:gray;'>Developed as part of Gen-AI Python 60-Day Challenge 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# ------------------------------------------------------------
# 📥 INPUT SECTION
# ------------------------------------------------------------
st.subheader("🧾 Step 1: Enter Expense Details")

col1, col2 = st.columns(2)
with col1:
    total_amount = st.number_input("💵 Total Expense (₹)", min_value=0.0, step=100.0, format="%.2f")
with col2:
    num_people = st.number_input("👥 Number of Friends", min_value=1, step=1)

st.markdown("---")
st.subheader("✍️ Step 2: Add Friends & Contributions (Optional)")

friends = []
total_contributed = 0.0

if num_people > 0:
    for i in range(int(num_people)):
        cols = st.columns([2, 1])
        with cols[0]:
            name = st.text_input(f"Friend {i+1} Name", value=f"Friend{i+1}", key=f"name_{i}")
        with cols[1]:
            contribution = st.number_input(
                f"{name}'s Contribution (₹)",
                min_value=0.0,
                step=50.0,
                key=f"contri_{i}",
                format="%.2f"
            )
        friends.append({"name": name, "contribution": contribution})
        total_contributed += contribution

# ------------------------------------------------------------
# 🧮 CALCULATION & RESULTS SECTION
# ------------------------------------------------------------
if st.button("💸 Calculate Split"):
    if total_amount <= 0:
        st.warning("⚠️ Please enter a valid total expense amount.")
    elif num_people <= 0:
        st.warning("⚠️ Number of friends should be at least 1.")
    else:
        st.markdown("---")
        st.subheader("📊 Step 3: Expense Summary")

        equal_share = total_amount / num_people

        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Total Bill", f"₹{total_amount:.2f}")
        col2.metric("👥 Total Friends", f"{num_people}")
        col3.metric("💸 Each Should Pay", f"₹{equal_share:.2f}")

        st.markdown("---")
        st.subheader("🧾 Step 4: Final Settlement Report")

        for f in friends:
            balance = f["contribution"] - equal_share
            if balance > 0:
                st.success(f"✅ {f['name']} should RECEIVE ₹{balance:.2f}")
            elif balance < 0:
                st.error(f"❌ {f['name']} should PAY ₹{-balance:.2f}")
            else:
                st.info(f"☑️ {f['name']} is perfectly settled!")

        # ------------------------------------------------------------
        # 🔍 VALIDATION CHECK
        # ------------------------------------------------------------
        st.markdown("---")
        diff = total_contributed - total_amount
        if abs(diff) > 0.01:
            st.warning(
                f"⚠️ Total Contributions (₹{total_contributed:.2f}) ≠ Total Bill (₹{total_amount:.2f})"
            )
            if diff > 0:
                st.info(f"💡 There is an extra ₹{diff:.2f} contributed.")
            else:
                st.error(f"💡 There is a shortage of ₹{-diff:.2f}.")
        else:
            st.success("✅ All contributions match the total bill exactly.")

        st.markdown("---")
        st.markdown(
            "<p style='text-align:center; color:green;'>🎉 Thank you for using Friends Expense Splitter! 💚</p>",
            unsafe_allow_html=True
        )

# ------------------------------------------------------------
# 📘 FOOTER
# ------------------------------------------------------------
st.markdown(
    """
    ---
    <div style='text-align:center; color:gray; font-size:13px'>
    💡 Built with ❤️ using <b>Python + Streamlit</b> | © 2025 Gen-AI Training
    </div>
    """,
    unsafe_allow_html=True
)
