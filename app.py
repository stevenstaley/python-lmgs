import streamlit as st
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta

# Calculate the date 75 years ago from today

min_date = date.today() - relativedelta(years=100)
pages = {
    "Screening": [
        st.Page("pages/1_screenings.py", title="Create New")],
    "SPOT": [
        st.Page("pages/2_spot.py", title="Create New")],
    "Interrogation": [
        st.Page("pages/4_ips.py", title="Interrogation Plans")],
    "Edit Dropdown Lists": [
        st.Page("pages/3_teamlist.py", title="Team and Personnel")]
    }

pg = st.navigation(pages, position="top")

pg.run()