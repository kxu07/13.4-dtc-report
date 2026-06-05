import streamlit as st

pages = {
    "Homepage": [
        st.Page("homepage.py", title="Home")
    ],
    "Report Sections": [
        st.Page("introduction.py", title="Introduction"),
        st.Page("users_requirements.py", title="Users and Requirements"),
        st.Page("design_concept_rationale.py", title="Design Concept and Rationale"),
        st.Page("limitations_next_steps.py",title="Limitations and Next Steps"),
        st.Page("conclusion.py", title="Conclusion"),
        st.Page("references.py", title="References")
    ],
    "Appendices": [
        st.Page("project_def.py", title="A. Project Definition"),
        st.Page("interviewing_summary.py", title="B. Interviewing Summary"),
        st.Page("market_research_summary.py", title="C. Market Research Summary"),
        st.Page("design_review_summary.py", title="D. Design Review Summary"),
        st.Page("instructions_for_construction.py", title="E. Instructions for Construction")
    ]
}

pg = st.navigation(pages)

pg.run()
