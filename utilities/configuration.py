import streamlit as st

def configure_page(pagetitle):
    """
    Sets the page configuration for the Streamlit app.
    """
    st.set_page_config(
        page_title=pagetitle,
        layout="wide"  # Use wide layout for better column view
    )

    st.markdown("""
        <style>
        .block-container {
            padding-top: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)