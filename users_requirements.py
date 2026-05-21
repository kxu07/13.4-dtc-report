import streamlit as st
from PIL import Image
import pandas as pd


st.title("Users and Requirements")

col1, col2 = st.columns(2)

st.subheader("Users")
st.write("Our solution is targeted towards casual pool players, people who play at public pool tables, and beginner pool players. The vast majority of amateur pool players don’t own their own pool cues and don’t know much about maintaining the tip. They may not own their own chalk or know much about how to apply or how much. This user group is our target, because we believe our product will help them the most and improve their playing experience—namely ensuring that they can adequately chalk their cue, easily and evenly. We did not include any high level/professional pool players because they usually own their own cues and know the best ways to take care of/switch out the tips of their pool cues. Professional pool players also are more familiar with the best ways to apply chalk and may prefer to use their own personal chalk. ")



st. subheader("Requirements")
st.write("Important needs: allows even chalk application, easy to use/intuitive, compliant with pool regulations, doesn’t damage pool cue")
st.write("Most importantly, our product needs to solve the core problem and provide an even chalk application. We want to make sure that people who have never seen our product can easily figure out how to use our product. Additionally, we want to make sure that anyone using our product is still compliant with the pool regulations set by the American Cue Sports handbook. Lastly, it is also important that our product doesn't damage the cue stick and doesn't have any adverse side effects.")