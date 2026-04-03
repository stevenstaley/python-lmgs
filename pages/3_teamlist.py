import streamlit as st
from utilities.functions import load_options, save_options
from utilities.configuration import configure_page
from utilities.options import TEAMS, PERSONNEL, RNS

configure_page("Teams and Personnel List")

st.title("Teams and Personnel")

# --- Functions to handle the file ---


# --- Page Content ---
col1, col2, col3 = st.columns(3)

with col1:
    # Load existing options to pre-fill the text area
    existing_options_text = load_options(TEAMS)
    
    # Text area for user to input/edit the options
    text_options = st.text_area(
        "Team Options",
        value=existing_options_text,
        height=300,
        help="Enter each dropdown option on a new line. You can add, edit, or remove options below. Each line will become a separate option in the dropdown list."
    )
    
    if st.button("Save Team Options"):
        # Save the current content of the text area to the file
        save_options(text_options, TEAMS)
        st.success(f"✅ Your dropdown options have been saved to {TEAMS}!")
        st.info("You can now go to the 'Main Page' to see the updated dropdown.")

with col2:
    # Load existing options to pre-fill the text area
    existing_options_text1 = load_options(PERSONNEL)
    
    # Text area for user to input/edit the options
    text_options1 = st.text_area(
        "Personnel Options",
        value=existing_options_text1,
        height=300,
        help="Enter each dropdown option on a new line. You can add, edit, or remove options below. Each line will become a separate option in the dropdown list."
    )
    
    if st.button("Save Personnel Options"):
        # Save the current content of the text area to the file
        save_options(text_options1, PERSONNEL)
        st.success(f"✅ Your dropdown options have been saved to `{PERSONNEL}`!")
        st.info("You can now go to the 'Main Page' to see the updated dropdown.")

with col3:
    # Load existing options to pre-fill the text area
    existing_options_text2 = load_options(RNS)
    
    # Text area for user to input/edit the options
    text_options2 = st.text_area(
        "Reporter Numbers",
        value=existing_options_text2,
        height=300,
        help="Enter each dropdown option on a new line. You can add, edit, or remove options below. Each line will become a separate option in the dropdown list."
    )
    
    if st.button("Save Reporter Numbers"):
        # Save the current content of the text area to the file
        save_options(text_options2, RNS)
        st.success(f"✅ Your dropdown options have been saved to `{RNS}`!")
        st.info("You can now go to the 'Main Page' to see the updated dropdown.")