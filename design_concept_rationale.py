import streamlit as st
from PIL import Image


st.title("Design Concept and Rationale")
st.subheader(
    "Design"
)
col1, col2 = st.columns(2)
with col1:
    st.image("mockup_view_1.png", "Figure __: Mockup front view")
with col2:
    st.image("mockup_view_2.png", "Figure __: Mockup back view")

st.subheader("Components")
#overview
st.write("Our product is essentially a semi-spherical piece of chalk on an applicator. " \
"It utilizes a semi-spherical piece of chalk to evenly apply chalk on all geometries of pool cue tips. " \
"The shroud surrounding the chalk is a guide to help the user understand how the product is supposed to be used." \
"These two components sit on an ergonomic handle for ease and comfort of use.")

#chalk
st.image("round_chalk.png", "Figure __: semi-spherical chalk")
st.write("The chalk itself is semi-spherical, instead of cube shaped like it traditionally is. The chalk is two centimeters in diameter. " \
"This is because the convex shape of the chalk will be able to evenly coat a dome shaped cue tip and a flat cue tip and everything in between. " \
"From our interviewing (see Appendix B), we saw that the current chalk shape is not sufficient, and that people do struggle to use the traditional chalk shapes. " \
"We decided to change the chalk shape to a semi-sphere to try to insure that all cue tip shapes could be effectively chalked.")

#shroud
st.write("The purpose of the shroud is the help guide the user in using the product. " \
"With the shroud, the user is guided to use the product in a circular motion and along the angles of the shroud itself. " \
"Additionally, with the feedback that we received in the design review (see Appendix D), we implemented a clear shroud material so that the user is able to see what they are doing. " \
"As an added bonus, the shroud helps to catch any chalk fallout and help catch chalk fragments if the user accidentally breaks the chalk.")

#handle
st.write("The handle is designed to contour with the shape of the user's hand. " \
"This gives the user a sensory cue on how to hold and use the product, along with making the product more comfortable to use.")