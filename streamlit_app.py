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
        st.Page("need_finding.py", title="A. Need Finding Research Summary"),
        st.Page("narrowing_down.py", title="B. Narrowing Down Research Summary"),
        st.Page("interviewing_summary.py", title="C. Interviewing Summary"),
        st.Page("market_research_summary.py", title="D. Market Research Summary")
    ]
}

pg = st.navigation(pages)

pg.run()
