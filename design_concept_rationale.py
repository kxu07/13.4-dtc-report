import streamlit as st
from PIL import Image


st.title("Design Concept and Rationale")
st.subheader(
    "Design"
)
st.write("Our product is a handheld cue tip chalker. It is composed of a handle, a shroud, and the chalk itself. " \
"The components are shown and labelled in Figure 7.")
st.image("chalk_pop_parts.png", "Figure 7: The Chalk Pop parts labelled")
col1, col2 = st.columns(2)

#overview
st.write("Our product is a semi-spherical piece of chalk surrounded by a shroud on an applicator. " \
"To evenly apply chalk on all different of pool cue tips shapes, the user utilizes circular motions around the chalk to reach all areas of the cue tip. " \
"The shroud surrounding the chalk is a guide to help build intuition on how the product is used, in circular motions around the semi-sphere." \
" These two components sit on a handle for the user to grip onto.")

st.subheader("Chalk")
#chalk
st.write("The chalk, as shown in Figure 8, is semi-spherical, instead of cube shaped like it traditionally is. The chalk is two centimeters in diameter. " \
"This is because the convex surface of the chalk will be able to evenly coat a dome shaped cue tip and a flat cue tip and everything in between. " \
"To form this chalk, we used a grinder to reshape the chalk from a cube to a semisphere (see Appendix E for more details). " \
"We decided to change the chalk shape to a semi-sphere to try to insure that all cue tip shapes could be effectively chalked.")
st.image("round_chalk.png", "Figure 8: semi-spherical chalk")


st.subheader("Shroud")
#shroud
st.write("The shroud fits around the chalk and is clear and cone-shaped, as seen in Figure 9. The purpose of the shroud is the help guide the user in using the product. " \
"With the shroud, the user is guided to use the product in a circular motion and along the angles of the shroud itself. " \
"The shroud itself is 3-D printed from clear PETG. " \
"Additionally, with the feedback that we received in the design review (see Appendix D), we implemented a clear shroud material so that the user is able to see what they are doing. " \
"As an added bonus, the shroud helps to catch any chalk fallout and help catch chalk fragments if the user accidentally breaks the chalk.")
st.image("shroud.png", "Figure 9: The shroud")

st.subheader("Handle")
#handle
st.write("The handle is designed to contour with the shape of the user's hand, as shown in Figure 10. ")
st.image("handle_hand.png", "Figure 10: Handle contoured to hand shape")
st.write("The handle 3-D printed from black PLA. This gives the user a sensory cue on how to hold and use the product, along with making the product more comfortable to use.")