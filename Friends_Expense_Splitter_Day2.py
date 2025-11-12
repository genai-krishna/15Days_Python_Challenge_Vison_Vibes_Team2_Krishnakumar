# ------------------------------------------------------------
# 💡 Project Name : Friends Expense Splitter
# 🎯 Purpose      : Split total expense among friends fairly
# 👨‍💻 Developer   : [Your Name]
# 🗓️ Context      : Gen-AI Python Training Daily Task
# ------------------------------------------------------------

# No extra libraries required, runs with plain Python
# ------------------------------------------------------------

def expense_splitter():
    print("\n💰 WELCOME TO FRIENDS EXPENSE SPLITTER 💰")
    print("------------------------------------------------------------")

    # 🧾 Step 1: Take total expense
    while True:
        try:
            total_amount = float(input("Enter the total expense amount (₹): "))
            if total_amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Please enter a valid positive amount!")

    # 👥 Step 2: Take number of friends
    while True:
        try:
            num_people = int(input("Enter number of friends: "))
            if num_people <= 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Please enter a valid positive number!")

    # ✍️ Step 3: Optionally add names & contributions
    print("\n(Optional) Enter each friend's name & contribution (press Enter to skip):")
    print("------------------------------------------------------------")

    friends = []
    total_contributed = 0

    for i in range(num_people):
        name = input(f"Friend {i+1} Name: ").strip() or f"Friend{i+1}"

        try:
            contribution = float(input(f"{name}'s Contribution (₹): ") or 0)
        except ValueError:
            contribution = 0

        friends.append({"name": name, "contribution": contribution})
        total_contributed += contribution

    # 💡 Step 4: Calculate equal share
    equal_share = total_amount / num_people

    print("\n------------------------------------------------------------")
    print(f"🧮 Total Bill: ₹{total_amount:.2f}")
    print(f"👥 Number of Friends: {num_people}")
    print(f"💸 Each Friend Should Pay: ₹{equal_share:.2f}")
    print("------------------------------------------------------------")

    # 🧾 Step 5: Show balance per person
    print("\n📊 Final Settlement Report:")
    print("------------------------------------------------------------")

    for f in friends:
        balance = f["contribution"] - equal_share
        if balance > 0:
            print(f"✅ {f['name']} should RECEIVE ₹{balance:.2f}")
        elif balance < 0:
            print(f"❌ {f['name']} should PAY ₹{-balance:.2f}")
        else:
            print(f"☑️ {f['name']} is settled up exactly!")

    # 🧩 Step 6: Validation check
    diff = total_contributed - total_amount
    if abs(diff) > 0.01:
        print("\n⚠️ Note: Total contributions (₹{:.2f}) ≠ Total bill (₹{:.2f})".format(total_contributed, total_amount))
    else:
        print("\n✅ All contributions match the total bill.")

    print("------------------------------------------------------------")
    print("🎉 Thank you for using Friends Expense Splitter!")
    print("------------------------------------------------------------")


# 🏁 Run the program
if __name__ == "__main__":
    expense_splitter()
