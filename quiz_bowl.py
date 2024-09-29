import streamlit as st
import random

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: #F4FADA;'"
             ">Quiz</span> <span style='color: #919A67;'>Bowl</span></h1>", unsafe_allow_html = True)

    questions = [
        {"question": "Compound interest can help grow your savings faster than simple interest.", "answer": True},
        {"question": "A budget helps you track your income and expenses.", "answer": True},
        {"question": "Credit scores only matter when applying for loans.", "answer": False},
        {"question": "Saving 20% of your income is a common recommendation for financial security.", "answer": True},
        {"question": "Investing in stocks is riskier than keeping money in a savings account.", "answer": True},
        {"question": "Having a diverse investment portfolio can reduce risk.", "answer": True},
        {"question": "Credit cards always charge interest on purchases.", "answer": False},
        {"question": "Emergency funds should cover at least three to six months of expenses.", "answer": True},
        {"question": "Debt should be paid off as quickly as possible to avoid interest.", "answer": True},
        {"question": "Financial literacy includes understanding how to read financial statements.", "answer": True},
        {"question": "Life insurance is only necessary for those with dependents.", "answer": False},
        {"question": "Retirement accounts often come with tax benefits.", "answer": True},
        {"question": "Paying only the minimum on your credit card will help improve your credit score.", "answer": False},
        {"question": "Real estate is typically considered a safe investment.", "answer": True},
        {"question": "You should review your financial goals at least once a year.", "answer": True},
        {"question": "All debt is bad and should be avoided.", "answer": False},
        {"question": "Setting financial goals can help motivate saving and investing.", "answer": True},
        {"question": "The stock market is a guaranteed way to make money.", "answer": False},
        {"question": "Annuities are a way to secure a steady income during retirement.", "answer": True},
        {"question": "Using public transportation can save you money compared to owning a car.", "answer": True},
        {"question": "Taxes do not apply to investments in a Roth IRA.", "answer": True},
        {"question": "Having too many credit cards can negatively affect your credit score.", "answer": True},
        {"question": "You can always get a loan without a credit history.", "answer": False},
        {"question": "Inflation can erode the purchasing power of your savings.", "answer": True},
        {"question": "Financial advisors are only for wealthy individuals.", "answer": False},
        {"question": "Understanding your net worth is an important aspect of financial literacy.", "answer": True},
        {"question": "It’s better to invest in a high-interest savings account than a diversified portfolio.", "answer": False},
        {"question": "A will is a document that outlines how your assets should be distributed after death.", "answer": True},
        {"question": "Paying off student loans early can save you money on interest.", "answer": True},
        {"question": "A 401(k) is a type of retirement savings plan offered by an employer.", "answer": True},
        {"question": "You should only consider investments with high potential returns.", "answer": False},
        {"question": "Cash flow management is essential for personal financial health.", "answer": True},
        {"question": "Financial education is only necessary for adults.", "answer": False},
        {"question": "Using credit wisely can build a positive credit history.", "answer": True}
    ]

    # initialize variables

    if 'selected_questions' not in st.session_state:
        st.session_state.selected_questions = random.sample(questions, 7)
        st.session_state.correct = 0
        st.session_state.attempted = 0
        st.session_state.user_answers = {idx: None for idx in range(7)}
        st.session_state.submit = False

    st.markdown("#### *Play a round of the financial literacy quiz bowl! "
                "You will be given seven questions - show us how well you know your finances!*")
    st.divider()

    # iterate through the selected questions

    for idx, q in enumerate(st.session_state.selected_questions):
        # Use radio button to select answers
        st.session_state.user_answers[idx] = st.radio(
            q["question"],
            options = ["True", "False"],
            index = None if st.session_state.user_answers[idx] is None else ["True", "False"].index(st.session_state.user_answers[idx])
        )

    # submit button to calculate results

    if st.button("Submit"):
        st.session_state.submit = True
        st.session_state.correct = 0

        for idx, q in enumerate(st.session_state.selected_questions):
            correct_answer = "True" if q["answer"] else "False"
            if st.session_state.user_answers[idx] == correct_answer:
                st.session_state.correct += 1

    # display results

    if st.session_state.submit:
        st.divider()
        percentage = (st.session_state.correct / len(st.session_state.selected_questions)) * 100
        st.markdown(f"#### You got {st.session_state.correct} questions correct out of "
                    f"{len(st.session_state.selected_questions)}! That is a {percentage:.2f}%.")

        # reset button to play again

        if st.button("Play Again"):

            st.session_state.clear()
            st.rerun()
