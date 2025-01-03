import streamlit as st
import requests
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

from modules.nav import SideBarLinks

# Initialize sidebar navigation
SideBarLinks()

# Base URL
BASE_URL = "http://api:4000/student"

# Function to call the `/add_employer_review` route (POST)
def add_employer_review(employer_id, review):
    try:
        response = requests.post(
            f"{BASE_URL}/add_employer_review",
            json={
                "employerId": employer_id,
                "review": review
            }
        )
        return response.json()
    except Exception as e:
        logger.error(f"Error while adding employer review: {e}")
        return {"error": "Failed to connect to the server"}


st.title("Employer Reviews Dashboard")


st.header("Add a New Employer Review")

# Input fields for employer review
employer_id = st.number_input("Employer ID", min_value=1, step=1)
review = st.text_area("Review Text")

if st.button("Add Review"):
    if employer_id and review.strip():
        result = add_employer_review(employer_id, review)
        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Review added successfully! Make note of Review ID to change/delete later.")
            st.json(result)
    else:
        st.error("Please fill in all fields.")
