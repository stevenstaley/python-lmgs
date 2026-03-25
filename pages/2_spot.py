import streamlit as st  
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta
from utilities.functions import get_options_from_file
# from utilities.functions import load_options, save_options
from utilities.configuration import configure_page
from utilities.options import TEAMS

min_date = date.today() - relativedelta(years=100)
configure_page("SPOT")
team_options = get_options_from_file(TEAMS)
# pg = st.navigation(pages, position="top")



# --- App Title ---

logo = "images/35m.png"

st.title("SPOT Report")

# --- Initialize Session State ---
# This holds the generated JSON so it doesn't disappear on rerun

if 'generated_spot_json' not in st.session_state:
    st.session_state.generated_spot_json = None

# --- Create Columns ---
col1, col2 = st.columns(2)

# --- Column 1: Data Entry ---
with col1:
    with st.container(border=True):
        team = st.selectbox("Team", options=team_options)
        who = st.text_input("Who")
        what = st.text_input("What")
        when = st.datetime_input("When", )
        where = st.text_input("Where")
        why = st.text_input("Why")
        how = st.text_area("How")
        other = st.text_area("Additional Information")
    email_body = f"""Team: {team}
Who: {who}
What: {what}
When: {when}
Where: {where}
Why: {why}
How: {how}
Additional Information: {other}
"""
with col2:
    st.text_area("Text for Email", email_body, height=300)

    if st.button("Generate JSON", type="primary"):
    # Create a Python dictionary from the input values
        output_data = {
            "report_type": "SPOT",
            "team": team,
            "who": who,
            "what": what,
            "when": when,
            "where": where,
            "why": why,
            "how": how,
            "additional_information": other
        }

        # Store the generated data in the session state

        st.session_state.generated_spot_json = output_data

    # Display the JSON from session state if it exists
    if st.session_state.generated_spot_json:
        generated_data = st.session_state.generated_spot_json
    else:
        generated_data = st.empty()
    if st.button("Save JSON to file"):
        folder_path = "spots/" + str(date.today())
        file_name = "SPOT" + "-" + str(when)
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
        if st.session_state.generated_spot_json:
            stcode = st.code(json.dumps(generated_data, indent=4, default=str), language='json')
        else:
            stcode = st.empty()
