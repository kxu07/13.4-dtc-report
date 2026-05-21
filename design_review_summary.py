import streamlit as st
import pandas as pd

st.title("Design Review Summary")

st.subheader("Introduction")
st.write("On Thursday, May 14, our team presented our current top two prototypes and our progress to the rest of the class and our professors to receive feedback. The two prototypes we presented were the guide tube vol. 2 and the sphere and shroud. We received a lot of good feedback, mostly consisting of practical/assembly questions as well as suggestions for different types of materials. We received the most feedback on the sphere and shroud prototype.")

st.subheader("Summary")
st.write("On the guide tube, the main feedback we received was that 1) we needed to be sure that the back and forth motion was actually the right motion and 2) that the middle of the chalk would wear much faster and still create a divot. ")
st.write("On the sphere and shroud, we received a lot more feedback. Below is a chart of the specific pieces of feedback, categorized into assembly questions, use questions, and evaluation questions.")

feedback_matrix = pd.DataFrame(
    {
        "Assembly": ["How to attach the sphere?", "Can you replace the sphere", "What material is the shroud", "Could different shroud materials improve perofrmance", "Where is the shroud chalk coming from?"],
        "Use": ["How would the sphere wear over time?", "What if the sphere itself could also rotate?", "Who would provide this product, players or venue?", "Could you grind up the chalk?", " "],
        "Evaluation": ["How to evaluate performance?", "Is there a qualitative vs quantitative way to judge product performance?", " ", " ", " "]
    }
)
st.dataframe(feedback_matrix,
              hide_index=True)
st.table(feedback_matrix)


st.subheader("Action Plan")
st.write("One of the most important pieces of feedback we received was to figure out a quantitative method to evaluate our product. While we had initially planned on using a qualitative method to evaluate performance—namely, visual inspection of the cue tip to see if the chalk had covered the cue evenly—the professors brought up that having a qualitative method for evaluation would give us more concrete feedback on our product. For now, we are planning on using a magnifying lens to inspect the cue tip and give it a percentage covered. A threshold that we think is sufficient for our prototype is 90 percent covered. ")
st.write("We were also concerned about being able to replace the chalk in our sphere and shroud prototype to make it reusable. To fix this, we thought of a new chalk replacement mechanism. The chalk will come fixed onto a rod that is able to lock into the handle of the product. When the chalk wears down, the user takes the entire rod out and puts in another rod with chalk fixed on the end. This way, creating a spherical chalk is not on the user, but on the manufacturer. Also, this design allows venues to only need to buy one shroud product, and be able to switch the chalk out when it runs out. ")
st.write("The material of the shroud was also something that we are looking into. We are planning to make prototypes with different materials to see how they perform. We are currently planning to test opaque hard plastic, clear hard plastic, and clear flexible plastic. We hypothesize that a clear plastic will help the user see what they’re doing. We want to see if a flexible plastic will help the user fit the cue tip into harder to reach areas around the chalk sphere. ")