import streamlit as st
import pandas as pd

st.title("Project Definition")

st.subheader("Mission Statement")
st.write("Recreational pool players struggle with reliably coating the tips of their cue sticks with chalk before shots, since the current chalk cubes have divots that don’t suit all pool cues, especially those present in game rooms and bars (hence, disproportionately affecting recreational players over professional), forcing players to constantly re chalk and also cause breakage of the chalk cubes. " \
"Our team will design a solution that enables a consistent, less wasteful chalk application that is also simple to use for the recreational pool player.")

st.subheader("Project Deliverables")
st.write("  - Final report")
st.write("  - Slide presentation during finals week")
st.write("  - Final prototype")

st.subheader("Design Constraints")

design_constrains = pd.DataFrame(
    {
        "Constraint": ["Accommodates standard cue tip geometry","No modification to the cue stick itself"],
        "Source": ["Industry standard across BCA equipment", "Inferred from user expectations "],
        "Rationale": ["This is our target user base", "Cue sticks are expensive, delicate pieces of kit that can't be altered "]
    }
)

st.table(design_constrains)

st.subheader("Users and Stakeholders")
st.write("*Prioritized by stake in the problem/solution*")
st.write("  1. Recreational pool players — primary users; interact with chalk every 1–3 shots during a game (based on user observation) ")
st.write("  2. Pool hall / bar / club operators — provide shared chalk to patrons; replace broken cubes.")
st.write("  3. Residence hall / dorm common-room managers (e.g., NU student housing) — supply pool as amenities")
st.write("  4. Chalk manufacturers — secondary stakeholder")

st.subheader("User Profile")
st.write("Primary user group — recreational pool players. A demographic and behavioral profile:")
st.write(" - Age range: 16-65, with higher proportion of 18-35 for bar/hall players")
st.write(" - Epxerience: Casual to intermediate. Not including professionals")
st.write(" - Setting: Bars, college dormitory common rooms, billiard halls, community centers, home game rooms")
st.write(" - Frequency of play: Irregular, weekly to a few times a year")
st.write(" - Equipment ownership: Majority use house cues; minority own personal cues")
st.write(" - Chalking behavior: Chalks between shots with cube chalk kept on the table rail; often shares chalk with other players")

st.subheader("Illustrative User Scenario")
st.write("*Based on a composite scenario drawing on team observations of pool tables in Northwestern dorm common rooms and Larson's secondary research on chalk application problems*")
st.write("JB is a 40 year old man playing pool with his two friends at the Mark II lounge. " \
"The table has only one, worn-down chalk cube that is missing one side. " \
"Between every 1-3 shots, JKB picks up the cube, rotates it over the tip and puts it back. " \
"The coverage on the tip is uneven, resulting in cue balls sometimes sliding off the stick when struck. " \
"Thus, JB is forced to apply harder and more frequently, leading to the tiny chalk cube crack.")

