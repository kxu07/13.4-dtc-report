import streamlit as st
from PIL import Image, ImageOps

st.title("Introduction")
st.subheader(
    "The problem and our solution"
)

st.subheader("The problem")
st.write("In most public pool halls/pool tables, the pool cues are not constantly being maintained, so the cue tip begins to wear down and lose its dome shape as seen in Figure 1, to a flatter tip as shown in Figure 2. " \
"Most pool chalks are made with a divot in the middle that fits a dome shaped cue as shown in Figure 3. ")
col1, col2 = st.columns(2)
with col1:
    st.image("dome_cuetip_intro.png", "Figure 1: Proper (dome-shaped) pool cue tip [1]")
with col2:  
   st.image("flat_cuetip_intro.png", "Figure 2: Worn down (flat top) cue tip [2]")
   st.image("chalk_intro.png", "Figure 3: Pool chalk (note dome cue tip shaped divot) [3]")
st.write("This geometric mismatch prevents flatter cue tips from being able to pick up chalk, as shown in Figure 4.")
st.image("geometric_mismatch.jpg", "Figure 4: Geometric mismatch between chalk and cue tip")
st.write("It is important to chalk your cue tip between shots so that players can utilize the friction between the cue and ball to generate spin, execute different shots, etc." \
" More advanced pool players may avoid this issue by replacing their cue tips or carrying their own chalk, but amateurs may not know how to do so or even that they are supposed to do so. ")
st.write("We wanted to create an intuitive and effective product that lets players chalk their cue evenly and easily, regardless of skill level.")

col1a, col2a = st.columns(2)

st.write("When using traditional pool chalk, the end result ends up looking more like Figure 4, with a bald spot in the middle.")
img = Image.open("uneven_chalk.JPG")
img = ImageOps.exif_transpose(img)
st.image(img, "Figure 5: Uneven pool chalk application w/ bald spot")
st.write("Evenly chalking your pool cue is important because it introduces rigid, abrasive particles that help increase friction between the smooth cue tip and smooth resin cue ball. " \
"Cue chalk can also fill in the microscopic gaps in the leather cue tip. " \
"These two factors prevent miscuing (the cue tip slipping along the cue ball), which helps with energy transfer, forward momentum, and rotational momentum allowing for more consistent shots. " \
"More advanced pool players may avoid the issue of uneven chalking by replacing their cue tips or carrying their own chalk, but amateurs may not know how to do so or even that they are supposed to do so.")



st. subheader("The solution")
st.image("chalk_pop.png", "Figure 6: The Chalk Pop")
st.write("Our solution is the Chalk Pop. " \
"It is a device that helps you chalk a cue tip of any geometry by utilizing a half-sphere shaped chalk. " \
"It has an ergonomic handle so that it is comfortable to use. " \
"The shroud surrounding the chalk helps guide the cue tip to get the right angles and an even chalk application.")
col1, col2 = st.columns(2)
