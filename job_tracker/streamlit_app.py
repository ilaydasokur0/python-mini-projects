import pandas as pd
import streamlit as st

from app.db import init_db, get_conn
from app.constants import STATUSES
from app.services import add_application, list_applications, top_skills
st.set_page_config(page_title="Job Tracker", layout="wide")

init_db()

st.title("Job Tracker")

tab1, tab2 = st.tabs(["➕ Add Application", "📊 Dashboard"])

with tab1:
    st.subheader("Add a new application")

    company = st.text_input("Company")
    role = st.text_input("Role")
    status = st.selectbox("Status", STATUSES, index=0)

    link = st.text_input("Link (optional)")
    notes = st.text_area("Notes (optional)", height=80)

    requirements_text = st.text_area(
        "Paste job requirements (optional)",
        height=200,
        placeholder="Paste the job posting requirements here..."
    )

    if st.button("Save", type="primary"):
        if not company.strip() or not role.strip():
            st.error("Company and Role are required.")
        else:
            app_id = add_application(
                company=company,
                role=role,
                status=status,
                requirements_text=requirements_text,
                link=link,
                notes=notes,
            )
            st.success(f"Saved! id = {app_id}")

with tab2:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Applications")

        filter_status = st.selectbox("Filter by status", ["All"] + STATUSES, index=0)
        rows = list_applications(None if filter_status == "All" else filter_status)

        if rows:
            df = pd.DataFrame([dict(r) for r in rows])
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No applications yet.")

    with col2:
        st.subheader("Top Skills")
        skill_rows = top_skills(10)

        if skill_rows:
            df_skills = pd.DataFrame([dict(r) for r in skill_rows])  # columns: skill, freq
            st.dataframe(df_skills, use_container_width=True, hide_index=True)
            st.bar_chart(df_skills.set_index("skill")["freq"])
        else:
            st.info("No skills yet. Add an application with requirements text.")