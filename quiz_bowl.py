import streamlit as st
import random

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: white;'"
             ">Quiz</span> <span style='color: olive;'>Bowl</span></h1>", unsafe_allow_html=True)

    questions = [
        {"question": "Credit cards can help improve your credit score.", "answer": True},
        {"question": "A budget is a financial plan for spending.", "answer": True},
        {"question": "Investing is only for wealthy individuals.", "answer": False},
        {"question": "The stock market is only for buying stocks.", "answer": False},
        {"question": "Saving money in a bank account is a good way to earn interest.", "answer": True},
        {"question": "A mortgage is a type of loan used to buy property.", "answer": True},
        {"question": "Insurance is unnecessary if you are healthy.", "answer": False},
        {"question": "You should always pay off your credit card balance in full.", "answer": True},
        {"question": "A 401(k) is a retirement savings plan.", "answer": True},
        {"question": "Compound interest can help grow your savings faster than simple interest.", "answer": True},
    ]

    # initialize variables

    if 'selected_questions' not in st.session_state:
        st.session_state.selected_questions = random.sample(questions, 7)
        st.session_state.correct = 0
        st.session_state.attempted = 0
        st.session_state.user_answers = {idx: None for idx in range(7)}
        st.session_state.submit = False

    st.write("Welcome to the financial literacy quiz bowl! "
             "You will be given 7 questions - show us how well you know your finances!")

    # iterate through the selected questions

    for idx, q in enumerate(st.session_state.selected_questions):
        # Use radio button to select answers
        st.session_state.user_answers[idx] = st.radio(
            q["question"],
            options=["True", "False"],
            index=None if st.session_state.user_answers[idx] is None else ["True", "False"].index(st.session_state.user_answers[idx])
        )

    # submit button to calculate results

    if st.button("Submit Quiz"):
        st.session_state.submit = True
        st.session_state.correct = 0

        for idx, q in enumerate(st.session_state.selected_questions):
            correct_answer = "True" if q["answer"] else "False"
            if st.session_state.user_answers[idx] == correct_answer:
                st.session_state.correct += 1

    # display results

    if st.session_state.submit:
        percentage = (st.session_state.correct / len(st.session_state.selected_questions)) * 100
        st.write(f"You got {st.session_state.correct} questions correct out of "
                 f"{len(st.session_state.selected_questions)}! That is {percentage:.2f}%.")

        # reset button to play again

        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
