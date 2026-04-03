import streamlit as st  
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta
from utilities.functions import get_options_from_file
# from utilities.functions import load_options, save_options
from utilities.configuration import configure_page
from utilities.options import TEAMS, PERSONNEL

min_date = date.today() - relativedelta(years=100)

configure_page("Screening")
# --- Page Content ---

# Get the list of options from the file
personnel_options = get_options_from_file(PERSONNEL)
team_options = get_options_from_file(TEAMS)
# pg = st.navigation(pages, position="top")



# --- App Title ---

logo = "images/35m.png"

st.title("Screening Report")

# --- Initialize Session State ---
# This holds the generated JSON so it doesn't disappear on rerun

if 'generated_json' not in st.session_state:
    st.session_state.generated_json = None

# --- Create Columns ---
col1, col2, col3, col4, col5 = st.columns(5)

# --- Column 1: Data Entry ---
with col1:
    with st.container(border=True):
        team = st.selectbox("Team", options=team_options)
        screener = st.selectbox("Screener", options=personnel_options)
        screendtg = st.datetime_input("Screening Date", value="now")
    with st.container(border=True):
        status = st.selectbox(
        "Status",
        ["Military", "Civilian", "Paramilitary", "Unknown"], index=None, placeholder="Select EPW Status"
    )
    with st.container(border=True):
        st.subheader("Capture Data")
        captdtg = st.datetime_input("Capture Date")
        isn = st.text_input("Capture Tag/ISN")
        pocapture = st.text_input("Place of Capture")
        capture_unit = st.text_input("Capturing Unit")
        capture_circ = st.text_area("Capture Circumstances")
        docs = st.checkbox("Documents?")
        docs_bool = False
        if docs:
            docdescription = st.text_area("Describe Documents")
            docs_bool = True
        else:
            docdescription = ""
        weapons = st.checkbox("Weapons?")
        weapons_bool = False
        if weapons:
            wpnsdescription = st.text_area("List Weapons")
            weapons_bool = True
        else:
            wpnsdescription = ""

    # --- Section 1: Personal Info ---
with col2:
    with st.container(border=True):
        st.subheader("Personal Info")
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        sex = st.selectbox(
        "Sex",
        ["Male", "Female", "Unknown"], index=None
    )
        dob = st.date_input("DOB", min_value=min_date)
        pob = st.text_input("POB")
        maritalstatus = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced", "Separated", "Widowed"], index=None
    )
    with st.container(border=True):
        st.subheader("Civilian")
        job = st.text_input("Job")
        org = st.text_input("Organization")
        duties = st.text_input("Duties")
        skills = st.text_input("Skills")

# --- Column 2: JSON Viewer ---

with col3:
    with st.container(border=True):
        st.subheader("Military")
        full_unit = st.text_input("Full Unit Designation")
        dty_psn = st.text_input("Duty Position")
        miljob = st.text_input("Military Job")
        branch = st.selectbox(
        "Branch",
        ["Army", "Air Force", "Navy", "Marine Corps", "Coast Guard", "Space", "Other"], index=None, placeholder="Select Military Branch")
        svcid = st.text_input("Service ID No")
        station = st.text_input("Station")
        milskills = st.text_input("Military Skills")
        milexp = st.text_input("Military Experience")

with col4:
    with st.container(border=True):
        st.subheader("Assesment Data")
        wounded = st.selectbox(
        "Wounded?",
        ["No", "Yes"], index=None
    )
        intelligencelevel = st.selectbox(
        "Intelligence Level",
        ["AVG", "AVG-", "AVG+"], index=None
    )
        remarks = st.text_area("Remarks")
        education = st.text_input("Education")
        mentcondition = st.text_input("Mental Condition")
        cooperation = st.select_slider(
        "Cooperation",
        options=[
            1, 2, 3,
        ],
    )
        knowledge = st.select_slider(
        "Knowledge",
        options=[
            "A", "B", "C"
        ],
    )
        assessment = st.text_area("Screener Assessment")
        approach = st.text_area("Approach Recommendations")

    # --- Generate Button ---

with col5:
    if st.button("Generate JSON", type="primary"):
    # Create a Python dictionary from the input values
        output_data = {
            "report_type": "Screening Report",
            "body": {
                "team": str(team),
                "screener": str(screener),
                "screening_date": str(screendtg),
                "status": str(status),
                "capture_data": {
                    "capture_tag_isn": str(isn),
                    "capture_date": str(captdtg),
                    "place_of_capture": str(pocapture),
                    "capturing_unit": str(capture_unit),
                    "capture_circumstances": str(capture_circ),
                    "documents": {
                        "docsyesorno": str(docs_bool),
                        "documents_description": str(docdescription)
                    },
                    "weapons": {
                        "wpnsyesorno": str(weapons_bool),
                        "weapons_description": str(wpnsdescription)
                    },
                "personal_info": {
                    "first_name": str(fname),
                    "last_name": str(lname),
                    "sex": str(sex),
                    "dob": str(dob),
                    "pob": str(pob),
                    "marital_status": str(maritalstatus)
                },
                "military": {
                    "full_unit_designation": str(full_unit),
                    "duty_position": str(dty_psn),
                    "job": str(miljob),
                    "branch": str(branch),
                    "service_id": str(svcid),
                    "station": str(station),
                    "military_skills": str(milskills),
                    "military_experience": str(milexp)
                },
                "civilian": {
                    "job": str(job),
                    "organization": str(org),
                    "duties": str(duties),
                    "skills": str(skills)
                },
                "assessment_data": {
                    "wounded": str(wounded),
                    "intelligence_level": str(intelligencelevel),
                    "remarks": str(remarks),
                    "education": str(education),
                    "mental_condition": str(mentcondition),
                    "cooperation": str(cooperation),
                    "knowledge": str(knowledge),
                    "screener_assessment": str(assessment),
                    "approach_recommendations": str(approach)
                }
        }}
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
        file_name = str(team) + "-" + str(isn) + "-" + str(fname) + "-" + str(lname) + str(captdtg) + "-" + str(screener)
        file_path = os.path.join(folder_path, f"{file_name}.json")
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Save the data to the file
        with open(file_path, "w") as f:
            json.dump(generated_data, f, indent=1, default=str)
        # Display a success message
        st.success(f"File successfully saved to: {file_path}")
    else:
        # Placeholder message
        json_dumps = json.dumps(generated_data, indent=4, default=str, ensure_ascii=False)
        # Also display as a raw code block for easy copying
        if st.session_state.generated_json:
            stcode = st.code(json_dumps)
        else:
            stcode = st.empty()
