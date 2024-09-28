# $mart app

import streamlit as st
#from streamlit_option_menu import option_menu

import home
import quiz_bowl
import savings_goals
import budgeting_tool
import motivation_board
import resources

st.sidebar.title("Where to?")
menu = st.sidebar.radio(
    "Take me to...",
    ("$mart",
     "Quiz Bowl",
     "Savings Goals",
     "Budgeting Tool",
     "Motivation Board",
     "Resources"),
    index = 0
)

def get_page():
    query = st.experimental_get_query_params()
    if 'page' in query:
        return query['page'][0]
    return None

if menu == "$mart":
    home.app()
elif menu == "Quiz Bowl":
    quiz_bowl.app()
elif menu == "Savings Goals":
    savings_goals.app()
elif menu == "Budgeting Tool":
    budgeting_tool.app()
elif menu == "Motivation Board":
    motivation_board.app()
elif menu == "Resources":
    resources.app()