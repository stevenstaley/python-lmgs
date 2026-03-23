import streamlit as st
import os

# Define the file path for storing options
OPTIONS_FILE_TEAMS = "dropdowns/teamlist.txt"
OPTIONS_FILE_PERSONNEL = "dropdowns/personnellist.txt"

st.set_page_config(layout="wide")

st.header("Teams and Personnel")

# --- Functions to handle the file ---
def load_options(FILE_PATH):
    """Reads options from the text file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            # Read lines and join them into a single string for the text_area
            return "\n".join([line.strip() for line in f.readlines()])
    return ""

def save_options(text_content, FILE_PATH):
    """Saves the given text content to the file."""
    with open(FILE_PATH, "w") as f:
        f.write(text_content)

# --- Page Content ---
col1, col2 = st.columns(2)

with col1:
    # Load existing options to pre-fill the text area
    existing_options_text = load_options(OPTIONS_FILE_TEAMS)
    st.write("Enter each dropdown option on a new line. You can add, edit, or remove options below.")
    
    # Text area for user to input/edit the options
    text_options = st.text_area(
        "Team Options",
        value=existing_options_text,
        height=300,
        help="Each line will become a separate option in the dropdown list."
    )
    
    if st.button("Save Team Options"):
        # Save the current content of the text area to the file
        save_options(text_options, OPTIONS_FILE_TEAMS)
        st.success(f"â Your dropdown options have been saved to {OPTIONS_FILE_TEAMS}!")
        st.info("You can now go to the 'Main Page' to see the updated dropdown.")

with col2:
    # Load existing options to pre-fill the text area
    existing_options_text1 = load_options(OPTIONS_FILE_PERSONNEL)
    
    st.write("Enter each dropdown option on a new line. You can add, edit, or remove options below.")
    
    # Text area for user to input/edit the options
    text_options1 = st.text_area(
        "Personnel Options",
        value=existing_options_text1,
        height=300,
        help="Each line will become a separate option in the dropdown list."
    )
    
    if st.button("Save Personnel Options"):
        # Save the current content of the text area to the file
        save_options(text_options1, OPTIONS_FILE_PERSONNEL)
        st.success(f"â Your dropdown options have been saved to `{OPTIONS_FILE_PERSONNEL}`!")
        st.info("You can now go to the 'Main Page' to see the updated dropdown.")