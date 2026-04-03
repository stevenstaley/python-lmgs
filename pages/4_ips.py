import streamlit as st  
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta
from utilities.functions import get_options_from_file
# from utilities.functions import load_options, save_options
from utilities.configuration import configure_page
from utilities.options import TEAMS, APPROACHES, PERSONNEL, RNS

min_date = date.today() - relativedelta(years=100)
configure_page("IP")
team_options = get_options_from_file(TEAMS)
approach_options = get_options_from_file(APPROACHES)
personnel_options = get_options_from_file(PERSONNEL)
rns_options = get_options_from_file(RNS)

logo = "images/35m.png"

st.title("IP")

# --- Initialize Session State ---
# This holds the generated JSON so it doesn't disappear on rerun

if 'generated_ip_json' not in st.session_state:
    st.session_state.generated_ip_json = None

# --- Create Columns ---
col1, col2, col3, col4 = st.columns(4)

# --- Column 1: Data Entry ---
with col1:
    with st.container(border=True):
        st.subheader("Interrogator")
        team = st.selectbox("Team", options=team_options)
        intgr = st.selectbox("Interrogator", options=personnel_options)
        linguist = st.text_input("Linguist")
        reporternumber = st.selectbox("Reporter Number", options=rns_options)
        startdtg = st.datetime_input("Start DTG")
        enddtg = st.datetime_input("End DTG")

with col2:
    with st.container(border=True):
        st.subheader("Detainee")
        isn = st.text_input("ISN")
        noti = st.number_input("Number of Times Interrogated", step=1)

        concerns = st.text_input("Concerns")
        app1select = st.selectbox("Approach 1", options=approach_options)
        app1 = st.text_area("Approach 1 Write-up")
        app2select = st.selectbox("Approach 2", options=approach_options)
        app2 = st.text_area("Approach 2 Write-up")
        app3select = st.selectbox("Approach 3", options=approach_options)
        app3 = st.text_area("Approach 3 Write-up")

with col3:
    with st.container(border=True):
        st.subheader("Intelligence")
        intobjs = st.text_area("Interrogation Objectives", help="""
        Include PIRs, Requirements, and other non intelligence related objectives for this session i.e., 'This interrogation will focus on (building rapport, follow up questioning on X topics, etc.)'
        """)
        questioningplan = st.text_area("Questioning Plan", help="Cover major questioning topics and requirements.\n***Describe HOW your approaches will support questioning for intelligence information.")

with col4:
    if st.button("Generate JSON", type="primary"):
    # Create a Python dictionary from the input values
        output_data = {
            "report_type": "IP",
            "body": {
                "interrogator": str(intgr),
                "linguist": str(linguist),
                "reporter_number": str(reporternumber),
                "start_dtg": str(startdtg),
                "end_dtg": str(enddtg),
                "isn": str(isn),
                "number_of_times_interrogated": str(noti),
                "objectives": str(intobjs),
                "questioning_plan": str(questioningplan),
                "concerns": str(concerns),
                "approaches": {
                    "approach_1": str(app1select),
                    "approach_1_writeup": str(app1),
                    "approach_2": str(app2select),
                    "approach_2_writeup": str(app2),
                    "approach_3": str(app3select),
                    "approach_3_writeup": str(app3)
                }
            }}

        # Store the generated data in the session state

        st.session_state.generated_ip_json = output_data

    # Display the JSON from session state if it exists
    if st.session_state.generated_ip_json:
        generated_data = st.session_state.generated_ip_json
    else:
        generated_data = st.empty()
    if st.button("Save JSON to file"):
        folder_path = "ips/" + str(date.today())
        file_name = "IP" + "-" + isn + "-" + intgr + "-" + str(startdtg) + "-" + str(noti)
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
        if st.session_state.generated_ip_json:
            stcode = st.code(json.dumps(generated_data, indent=4, default=str), language='json')
        else:
            stcode = st.empty()
