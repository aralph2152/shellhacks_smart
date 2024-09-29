# savings goals page

import streamlit as st
from datetime import datetime

def app():

    def calculate_savings(total_cost, target_date, freq):
        # Calculate how many days, weeks, or months until the target date
        today = datetime.now()
        target = datetime.strptime(target_date, "%Y-%m-%d")
        time_remaining = (target - today).days

        if time_remaining <= 0:
            return None  # Target date has passed

        if freq == 'Daily':
            return total_cost / time_remaining
        elif freq == 'Weekly':
            return total_cost / (time_remaining / 7)
        elif freq == 'Monthly':
            return total_cost / (time_remaining / 30)  # Approximate months

    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: #F4FADA;'"
             ">Savings</span> <span style='color: #919A67;'>Goals</span></h1>", unsafe_allow_html = True)
    st.markdown("#### *Use this tool to set your savings goals and determine how "
                "much you need to save regularly in order to reach them by your desired date.*")
    st.divider()

    # Input fields
    item_name = st.text_input("What are you saving for?")
    goal_cost = st.number_input("Total cost of the item ($):", min_value = 0.0, format = "%.2f")
    target_date = st.date_input("By when do you want to reach your goal?", value = datetime.now())
    freq = st.selectbox("Choose how often you want to see your savings plan:", ('Daily', 'Weekly', 'Monthly'))

    # Calculate savings plan
    if st.button("Calculate Savings Goal"):
        st.divider()
        total_cost = goal_cost
        target_date_str = target_date.strftime("%B %d, %Y")
        target_date_iso = target_date.strftime("%Y-%m-%d")
        required_savings = calculate_savings(total_cost, target_date_iso, freq)

        if required_savings is not None:
            st.write(
                f"#### You need to save ${required_savings:.2f} {freq.lower()} in order to reach your goal by {target_date_str}.")
        else:
            st.write("The target date has already passed. Please choose a future date.")

        st.write("✦ Be sure to set realistic savings goals! The best way to make sure that your goals "
                "are met is to make them achievable. Feel free to adjust your inputs and reset as needed!")
        if st.button("Reset"):
            st.rerun()
