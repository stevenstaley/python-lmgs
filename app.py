# Installing collected packages: watchdog, tzdata, typing-extensions, tornado, toml, tenacity, smmap, pyarrow, protobuf, numpy, narwhals, cachetools, pydeck, pandas, gitdb, altair, gitpython, streamlit


import streamlit as st
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta

# Calculate the date 75 years ago from today

min_date = date.today() - relativedelta(years=100)

pages = {

    "Your account": [

        st.Page("pages/1_screening.py", title="Test App"),

        st.Page("pages/2_test_app.py", title="Nope")

    ]

}

pg = st.navigation(pages, position="top")

pg.run()

# --- Page Configuration ---

st.set_page_config(

    page_title="JSON Generator",

    layout="wide"  # Use wide layout for better column view

)

# pg = st.navigation(pages, position="top")

st.markdown("""

    <style>

    .block-container {

        padding-top: 2rem;

    }

    </style>

    """, unsafe_allow_html=True)
