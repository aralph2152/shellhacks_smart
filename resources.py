# resources page

import streamlit as st

def app():
    st.write("<h1 style='font-weight: bold; font-style: italic;'><span style='color: #F4FADA;'"
             ">RE:</span> <span style='color: #919A67;'>Sources</span></h1>", unsafe_allow_html = True)

    st.markdown("#### *Resources for you*")
    st.markdown(
        "<a href='https://www.occ.gov/topics/consumers-and-communities/"
        "community-affairs/resource-directories/financial-literacy/"
        "index-financial-literacy-resource-directory.html' target='_blank'>"
        "View the OCC Financial Literacy Resource Directory</a></p>",
        unsafe_allow_html = True
    )
    st.markdown(
        "<a href='https://corporate.vanguard.com/content/corporatesite/us/en/corp/"
        "articles/financial-literacy-and-wellness-two-peas-in-a-pod.html'>"
        "Financial Literacy and Financial Wellness from Vanguard </a></p>",
        unsafe_allow_html = True
    )
    st.markdown(
        "<a href='https://www.finra.org/financial_literacy_quiz' target='_blank'>"
        "Take the FINRA Financial Literacy Quiz</a></p>",
        unsafe_allow_html = True
    )
    st.markdown(
        "<a href='https://ncua.gov/consumers/financial-literacy-resources'>"
        "Visit the NCUA Financial Literacy & Education Center</a></p>",
        unsafe_allow_html=True
    )
    st.divider()


    st.markdown("#### *Resources we used*")
    st.markdown("Lusardi, A. Financial literacy and the need for financial education: evidence and implications. "
                "Swiss J Economics Statistics 155, 1 (2019). https://doi.org/10.1186/s41937-019-0027-5")
    st.markdown("“National Financial Capability Study.” Global Financial Literacy Excellence Center (GFLEC), "
                "11 Jan. 2023, gflec.org/initiatives/national-financial-capability-study/. ")
    st.markdown("Puelz, D., & Puelz, R. (2022). Financial Literacy and Perceived Economic Outcomes. "
                "Statistics and Public Policy, 9(1), 122–135. https://doi.org/10.1080/2330443X.2022.2086191")
    st.markdown("Streeter JL. Financial literacy and financial well-being: Evidence from the US. "
                "Journal of Financial Literacy and Wellbeing. 2023;1(2):169-198. doi:10.1017/flw.2023.13")
    st.divider()
