import streamlit as st  
import json
from datetime import date
import os
from dateutil.relativedelta import relativedelta

min_date = date.today() - relativedelta(years=100)

st.set_page_config(
    page_title="JSON Generator",
    layout="wide"  # Use wide layout for better column view
)

st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

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
        screener = st.text_input("Screener")
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

            "screener": screener,

            "screening_date": screendtg,

            "status": status,

            "capture_data": {

                "capture_tag_isn": isn,

                "capture_date": captdtg,

                "place_of_capture": pocapture,

                "capturing_unit": capture_unit,

                "capture_circumstances": capture_circ,

                "documents": {

                    "docsyesorno": docs_bool,

                    "documents_description": docdescription

                },

                "weapons": {

                    "wpnsyesorno": weapons_bool,

                    "weapons_description": wpnsdescription

                },

            "personal_info": {

                "first_name": fname,

                "last_name": lname,

                "sex": sex,

                "dob": dob,

                "pob": pob,

                "marital_status": maritalstatus

            },

            "military": {

                "full_unit_designation": full_unit,

                "duty_position": dty_psn,

                "job": miljob,

                "branch": branch,

                "service_id": svcid,

                "station": station,

                "skills": milskills,

                "military_experience": milexp

            },

            "civilian": {

                "job": job,

                "organization": org,

                "duties": duties,

                "skills": skills

            },

            "assessment_data": {

                "wounded": wounded,

                "intelligence_level": intelligencelevel,

                "remarks": remarks,

                "education": education,

                "mental_condition": mentcondition,

                "cooperation": cooperation,

                "knowledge": knowledge,

                "screener_assessment": assessment,

                "approach_recommendations": approach

            }

    }

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