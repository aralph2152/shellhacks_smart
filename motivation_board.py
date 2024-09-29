# motivation board page

import streamlit as st
import random

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: #F4FADA;'"
             ">Motivation</span> <span style='color: #919A67;'>Board</span></h1>", unsafe_allow_html=True)
    st.markdown("#### *Feeling like you need a little motivation? Let one of our inspirational quotes guide your day.*")
    st.divider()

    # define the list of 50 inspirational/financial quotes

    quotes = [
        "Believe in your financial potential, and the world will believe in it too.",
        "Invest in yourself; it pays the best interest.",
        "Saving is the first step towards wealth.",
        "Budgeting is not about limiting yourself; it's about making room for your priorities.",
        "The best time to plant a tree was 20 years ago. The second-best time is now.",
        "You don't need to be a genius to build wealth; you just need a plan.",
        "Your wealth is in your habits.",
        "Financial freedom is available to those who learn about it and work for it.",
        "A penny saved is a penny earned.",
        "Never spend your money before you have it.",
        "The goal isn’t more money. The goal is living life on your terms.",
        "Every time you borrow money, you’re robbing your future self.",
        "Do not save what is left after spending, but spend what is left after saving.",
        "Money is a tool. It will take you wherever you wish, but it won’t replace you as the driver.",
        "Wealth consists not in having great possessions, but in having few wants.",
        "An investment in knowledge pays the best interest.",
        "Financial fitness is not a pipe dream or a state of mind—it’s a reality if you are willing to pursue it and embrace it.",
        "The quickest way to double your money is to fold it in half and put it back in your pocket.",
        "Being rich is having money; being wealthy is having time.",
        "It’s not about having a lot of money. It’s about knowing how to manage it.",
        "Money never made a man happy yet, nor will it. The more a man has, the more he wants.",
        "Small daily improvements over time lead to stunning results.",
        "The habit of saving is itself an education; it fosters every virtue, teaches self-denial, cultivates the sense of order, trains forethought, and so broadens the mind.",
        "Your income can grow only to the extent that you do.",
        "The secret to wealth is simple: spend less than you earn and invest the difference.",
        "You must gain control over your money, or the lack of it will forever control you.",
        "The stock market is filled with individuals who know the price of everything, but the value of nothing.",
        "Never depend on a single income. Make an investment to create a second source.",
        "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "Don’t look for the needle in the haystack. Just buy the haystack.",
        "Price is what you pay. Value is what you get.",
        "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs.",
        "The four most dangerous words in investing are: ‘this time it’s different.’",
        "The biggest risk of all is not taking one.",
        "The goal is not to be rich. The goal is to be financially free.",
        "In investing, what is comfortable is rarely profitable.",
        "Wealth is the ability to fully experience life.",
        "Compound interest is the eighth wonder of the world. He who understands it, earns it... he who doesn’t... pays it.",
        "It is not the man who has too little, but the man who craves more, that is poor.",
        "Financial freedom is freedom from fear.",
        "Financial independence is about having more choices.",
        "Building wealth is a marathon, not a sprint. Discipline is the key.",
        "The art is not in making money, but in keeping it.",
        "Time is more valuable than money. You can get more money, but you cannot get more time.",
        "It’s not your salary that makes you rich; it’s your spending habits.",
        "The only place where success comes before work is in the dictionary.",
        "Don’t let making a living prevent you from making a life.",
        "Money, like emotions, is something you must control to keep your life on the right track."
    ]

    # button to generate a new quote

    if st.button("Generate a Quote"):
        quote = random.choice(quotes)
        st.markdown(f"<h3 style='color:#919A67; font-style:italic;'>{quote}</h3>", unsafe_allow_html = True)
    st.divider()