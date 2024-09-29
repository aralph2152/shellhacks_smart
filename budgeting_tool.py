import streamlit as st
import plotly.graph_objects as go

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: white;'"
             ">Budgeting</span> <span style='color: olive;'>Tool</span></h1>", unsafe_allow_html=True)
    st.markdown("#### *Try out a new budget and help visualize where your money goes with the budgeting tool*")
    st.divider()

    st.write("""
    Budgeting is a powerful tool that allows you to plan your finances according to your unique needs and goals.
    A popular budgeting framework is the **50/30/20 rule**, where:
    ✦ **50%** of your income goes towards *Needs* (e.g., rent, groceries, bills),
    ✦ **30%** is allocated to *Wants* (e.g., entertainment, dining out), and
    ✦ **20%** goes towards *Financial Freedom* (e.g., savings, paying off debt).
    """)

    # user input

    st.header("Monthly Expenses")
    monthly_income = st.number_input("What is your total monthly income?", value=0)

    col1, col2 = st.columns(2)

    with col1:
        rent = st.number_input("Rent / Mortgage", value=0)
        groceries = st.number_input("Groceries", value=0)
        bills = st.number_input("Utilities / Bills", value=0)
        misc_necessary = st.number_input("Other Necessary Expenses", value=0)

    with col2:
        wants = st.number_input("Wants (Dining out, Entertainment, etc.)", value=0)
        savings = st.number_input("Savings", value=0)
        debt_repayment = st.number_input("Debt Repayment", value=0)
        miscellaneous = st.number_input("Miscellaneous", value=0)

    # merge categories

    needs_total = rent + groceries + bills + misc_necessary
    wants_total = wants + miscellaneous
    financial_freedom_total = savings + debt_repayment

    # percentages in relation to income

    if monthly_income > 0:
        user_budget_percentages = [
            needs_total / monthly_income * 100,
            wants_total / monthly_income * 100,
            financial_freedom_total / monthly_income * 100
        ]
    else:
        user_budget_percentages = [0, 0, 0]

    # make benchmarks

    benchmark_percentages = [50, 30, 20]

    # make a bar chart

    categories = ['Needs', 'Wants', 'Financial Freedom']
    user_budget_values = user_budget_percentages + [needs_total, wants_total, financial_freedom_total]
    benchmark_values = benchmark_percentages + [monthly_income * benchmark_percentages[0] / 100,
                                                monthly_income * benchmark_percentages[1] / 100,
                                                monthly_income * benchmark_percentages[2] / 100]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=benchmark_percentages,
        name='50/30/20 Benchmark',
        marker_color='lightgreen',
        text=benchmark_percentages,
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=user_budget_percentages,
        name='Your Budget',
        marker_color='darkgreen',
        text=user_budget_percentages,
        textposition='auto'
    ))

    fig.update_layout(
        title='Budget Breakdown: 50/30/20 Benchmark vs. Your Budget',
        xaxis_title='Categories',
        yaxis_title='Percentage of Income (%)',
        barmode='group',
        legend_title='Budget Type',
        margin=dict(t=50, l=25, r=25, b=25)
    )

    st.plotly_chart(fig)

    # give budget recommendations

    st.header("Budget Analysis and Recommendations")
    remaining_balance = monthly_income - (needs_total + wants_total + financial_freedom_total)
    st.write(f"### Remaining Balance: ${remaining_balance:.2f}")

    if remaining_balance < 0:
        st.warning(f"You're overspending by ${-remaining_balance:.2f}. Consider reducing spending in some categories.")
    else:
        st.success("You're within your budget! Great job!")

    if user_budget_percentages[0] > 50:
        st.warning("Your spending on Needs exceeds the recommended 50%. Try reducing necessary expenses where possible.")
    if user_budget_percentages[1] > 30:
        st.warning("Your spending on Wants exceeds the recommended 30%. Consider cutting down on discretionary spending.")
    if user_budget_percentages[2] < 20:
        st.info("You're not allocating 20% towards Financial Freedom. Consider increasing your savings or debt repayment.")
