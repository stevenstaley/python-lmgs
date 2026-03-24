import streamlit as st

pages = {
    "Screening": [
        st.Page("pages/1_screenings.py", title="Create New")],
    "SPOT": [
        st.Page("pages/2_spot.py", title="Create New")],
    "Edit Dropdown Lists": [
        st.Page("pages/3_teamlist.py", title="Team and Personnel")]
    }

pg = st.navigation(pages, position="top")

pg.run()
