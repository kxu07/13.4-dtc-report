import streamlit as st
import pandas as pd

st.title("List of Tables and Figures")

st.subheader("List of Tables")
tables = pd.DataFrame(
    {
        "Table": ["Design Constraints", "Design Feedback", "Bill of materials"],
        "Location": ["Appendix A: Project Definition", "Appendix D: Design Review Summary", "Appendix E: Instructions for Construction"]
    }
)
st.table(tables)

st.subheader("List of Figures")
figures = pd.DataFrame(
    {
        "Figure": ["Figure 1: The Chalk Pop", "Figure 2: Proper (dome-shaped) pool cue tip", "Figure 3: Worn down(flat top) cue tip", "Figure 4: Pool chalk", "Figure 5: Geometric mismatch between chalk and cue tip", "Figure 6: Uneven pool chalk application w/ bald spot", "Figure 7: The Chalk Pop", "Figure 8: The Chalk Pop components", "Figure 9: Semi-spherical chalk", "Figure 10: The shroud", "Figure 11: Handle contoured to hand shape", "Figure 12: Keychain pool chalk holder", "Figure 13: Poolgods tip tool square pocket chalker", "Figure 14: Cuetex chalker and cue tip pick", "Figure 15: Universal round chalk", "Figure 16: The Chalk Pop construction", "Figure 17: Shaping chalk with bench sander", "Figure 18: The chalk sanded halfway", "Figure 19: The final round chalk", "Figure 20: The chalk in the shroud", "Figure 21: The completed Chalk Pop", "Figure 22: The recommended Chalk Pop grip"],
        "Location": ["Executive Summary", "Introduction", "Introduction", "Introduction", "Introduction", "Introduction", "Introduction", "Design Concept and Rationale", "Design Concept and Rationale", "Design Concept and Rationale", "Design Concept and Rationale", "Appendix C: Market Research Summary",  "Appendix C: Market Research Summary",  "Appendix C: Market Research Summary",  "Appendix C: Market Research Summary", "Appendix E: Instructions for Construction", "Appendix E: Instructions for Construction", "Appendix E: Instructions for Construction", "Appendix E: Instructions for Construction", "Appendix E: Instructions for Construction", "Appendix E: Instructions for Construction", "Appendix F: Instructions for Use"]
    }
)

st.table(figures)
