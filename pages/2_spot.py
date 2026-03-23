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
col1, col2, col3 = st.columns(3)

# --- Column 1: Data Entry ---
with col1:
    
with col2:

with col3:
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

