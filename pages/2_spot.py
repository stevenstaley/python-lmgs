import streamlit as st  
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta

min_date = date.today() - relativedelta(years=100)

st.set_page_config(
    page_title="SPOT",
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

# --- App Title ---

logo = "images/35m.png"

st.title("SPOT Report")

# --- Initialize Session State ---
# This holds the generated JSON so it doesn't disappear on rerun

if 'generated_json' not in st.session_state:
    st.session_state.generated_json = None

# --- Create Columns ---
col1, col2 = st.columns(2)

# --- Column 1: Data Entry ---
with col1:
    with st.container(border=True):
        who = st.text_input("Who")
        what = st.text_input("What")
        when = st.datetime_input("When")
        where = st.text_input("Where")
        why = st.text_input("Why")
        how = st.text_area("How")
        other = st.text_area("Additional Information")

with col2:
    st.write(f"""
        Who: {who}
        What: {what}
        When: {when}
        Where: {where}
        Why: {why}
        How: {how}
        Other: {other}
        """)
    if st.button("Generate JSON", type="primary"):
    # Create a Python dictionary from the input values
        output_data = {
            "report_type": "SPOT",
            "who": who,
            "what": what,
            "when": when,
            "where": where,
            "why": why,
            "how": how,
            "additional_information": other
        }

        # Store the generated data in the session state

        st.session_state.generated_json = output_data

    # Display the JSON from session state if it exists
    if st.session_state.generated_json:
        generated_data = st.session_state.generated_json
    else:
        generated_data = st.empty()
    if st.button("Save JSON to file"):
        folder_path = "screenings/" + str(date.today())
        file_name = isn + "-" + fname + "-" + lname + str(captdtg) + "-" + screener
        file_path = os.path.join(folder_path, f"{file_name}.json")
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Save the data to the file
        with open(file_path, "w") as f:
            json.dump(generated_data, f, indent=4, default=str)
        # Display a success message
        st.success(f"File successfully saved to: {file_path}")
    else:
        # Placeholder message
        json_dumps = json.dumps(generated_data, indent=4, default=str)
        # Also display as a raw code block for easy copying
        if st.session_state.generated_json:
            stcode = st.code(json.dumps(generated_data, indent=4, default=str), language='json')
        else:
            stcode = st.empty()

