# home page

import streamlit as st

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: #F4FADA;'"
             ">Welcome to </span> <span style='color: #919A67;'>get$mart.</span></h1>", unsafe_allow_html = True)
    st.markdown("### *Start taking your first steps towards financial freedom.*")
    st.divider()

    # why $mart

    st.markdown("#### ***Why get$mart?***")
    st.write("✦ get$mart helps you better understand your level of financial literacy, which allows you to make "
             "better decisions, save more efficiently, and achieve financial freedom faster than ever before! ")
    st.divider()

    # financial literacy quiz

    st.markdown("#### ***How Do You Stack Up?***")
    st.write("✦ The following seven questions are from the FINRA Financial Literacy Quiz. "
             "How many can you get correct?")

    st.session_state.correct = 0
    if 'submit' not in st.session_state:
        st.session_state.submit = False

    q1 = st.radio(
        "Suppose you have $100 in a savings account earning 2 percent interest "
        "a year. After five years, how much would you have?",
        options = ["More than \$102",
                 "Exactly \$102",
                 "Less than \$102",
                 "I don't know"
                 ],
        index = None
    )
    if q1 == "More than \$102":
        st.session_state.correct += 1

    q2 = st.radio(
        "Imagine that the interest rate on your savings account is 1 percent a year "
        "and inflation is 2 percent a year. After one year, would the money in the account "
        "buy more than it does today, exactly the same or less than today?",
        options = [
            "More",
            "Same",
            "Less",
            "I don't know"
        ],
        index = None
    )
    if q2 == "Less":
        st.session_state.correct += 1

    q3 = st.radio(
        "If interest rates rise, what will typically happen to bond prices? "
        "Rise, fall, stay the same, or is there no relationship?",
        options = [
            "Rise",
            "Fall",
            "Stay the Same",
            "No Relationship",
            "I don't know"
        ],
        index = None
    )
    if q3 == "Fall":
        st.session_state.correct += 1

    q4 = st.radio(
        "A 15-year mortgage typically requires higher monthly payments than a 30-year "
        "mortgage but the total interest over the life of the loan will be less.",
        options = [
            "True",
            "False",
            "I don't know"
        ],
        index = None
    )
    if q4 == "True":
        st.session_state.correct += 1

    q5 = st.radio(
        "Buying a single company's stock usually provides a safer return than a stock mutual fund.",
        options = [
            "True",
            "False",
            "I don't know"
        ],
        index = None
    )
    if q5 == "False":
        st.session_state.correct += 1

    q6 = st.radio(
        "Suppose you owe $1,000 on a loan and the interest rate you are charged is "
        "20% per year compounded annually. If you didn't pay anything off, at this interest rate, "
        "how many years would it take for the amount you owe to double?",
        options = [
            "Less than 2 years",
            "2 to 4 years",
            "5 to 9 years",
            "10 or more years",
            "I don't know"
        ],
        index = None
    )
    if q6 == "2 to 4 years":
        st.session_state.correct += 1

    q7 = st.radio(
        "Which of the following indicates the highest probability of getting a particular disease?",
        options = [
            "There is a one-in-twenty chance of getting the disease",
            "2% of the population will get the disease",
            "25 out of every 1,000 people will get the disease",
            "I don't know"
        ],
        index = None
    )
    if q7 == "There is a one-in-twenty chance of getting the disease":
        st.session_state.correct += 1

    if st.button("Submit Quiz"):
        st.session_state.submit = True

    if st.session_state.submit == True:
        percentage = (st.session_state.correct / 7) * 100
        if st.session_state.submit == True:
            percentage = (st.session_state.correct / 7) * 100
            st.write(f"You got {st.session_state.correct} questions correct out of 7! That is {percentage:.2f}%.")
            st.write("So, how do you stack up? Would you consider yourself financially literate?")

    if getattr(st.session_state, 'submit', False):
        if st.button("Yes!"):
            st.write("That's awesome! Using $mart tools can help you maintain your financial literacy "
                     "and support you in making better financial decisions!")
        if st.button("Almost..."):
            st.write("You're on your way to a brighter financial future! By using $mart tools, you can learn more "
                     "about financial terminology and practices to increase your financial literacy and "
                     "move towards a future of financial freedom!")
        if st.button("Not yet."):
            st.write("That's okay! Using $mart tools can help introduce you to a variety of "
                     "terms, practices, and concepts which can help you feel more confident "
                     "in your financial literacy and decision making skills.")

    # display average stats

    st.divider()

    st.markdown("#### ***What steps can you take?***")
    st.write("Progressing towards a more secure financial future can be intimidating,  "
             "but taking small steps towards your goals can make a big difference! "
             "Use the navigation bar on the left to access get$mart features.")
    st.write("✦ Understand financial terminology by playing a round of get$mart quiz bowl")
    st.write("✦ Create a savings goal using the get$mart goal guide")
    st.write("✦ Outline a new budget with the get$mart budgeting tool")
    st.write("✦ Try out the get$mart motivation board to keep yourself accountable")
    st.write("✦ Check out our get$mart resources to learn more")
    st.divider()
