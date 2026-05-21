import streamlit as st
from PIL import Image

st.title("Narrowing down process research")
st.subheader("Dorm doors lack dampers")
st.write("Many commercial solutions exist: ")

col1, col2 = st.columns(2)
 
with col1:
    st.image("door_damper_1.png")

with col2:
    st.image("door_damper_2.png")

st.write("Many patents also exist:")

st.image("damper_patent_1.png", "Patent: CN101680254BCN101680254B")
st.image("damper_patent_2.png", "Patent: US8806718B2")

st.write("There are many solutions that already exist. Some are more focused on add-ons like the patent above, and others are focused on creating friction within the hinge like the product on the top right. The price range for these solutions is in the 100 dollar range.")
st.write("These solutions are sub-optimal for the following reasons. They usually require power tools and equipment for installation and usually are permanent/will leave a mark, which is not allowed in many dorms. They’re also a bit expensive for the target audience we’re looking at, which is college students and other students that live in dorms (boarding school etc).")
st.write("We decided to pass on this idea, because there are many existing solutions that universities and schools could implement on a mass scale. ")

st.subheader("Safety glasses don't fit a variety of noses")

col1a, col2a = st.columns(2)
with col1a:
    st.image("safety_glasses_patent.png", "Patent: CN103097939A")
with col2a: 
    st.write("Many people on reddit threads have the same problem. The problem is that many Asian people have a low nose bridge, and pretty much everyone else has a high nose bridge, so there is a gap in the market for safety glasses for low nose bridge people especially in the US.")
st.write("There are some existing solutions. Some companies like Oakley or 3M offer different nose bridge fits for their glasses lines. However, if labs were to use these solutions, they would need to buy separate glasses for separate people, which could lead to shortages in glasses types. These glasses are also on the more expensive side, costing up to 200 dollars, which could strain people/labs on a budget.")

st.subheader("Uneven pool chalk application")
st.write("Problem: It is difficult to get pool chalk on the tip of a cue stick and pool chalk breaks easily")
st.write("Existing patents:")
col1b, col2b = st.columns(2)
with col1b:
    st.image("chalk_patent_1.png","Electronic chalk applicator")
with col2b:
    st.image("chalk_patent_2.png", "Chalk raising device")

st.write("Many solutions exist, but they are not ideal. The electronic chalk applicator is a motorized rotating chalk block that applies chalk automatically when the cue tip is inserted. However, it requires a power source and is stationery (not portable or practical). The chalk raising device could be useful when designing a solution that may require chalk to be pushed up as it wears down. It addresses waste, but it does not really address the core issue, chalk application.")

st.subheader("Deadlift plate difficulty")
st.write("Problem: It is difficult to rack plates onto a barbell for deadlift")
st.write("Many patents exist for this: ")
st.write("   - US8992394: Barbell Jack Stand with Lever ")
st.write("   - US7637852: Barbell Ramp Stand")
st.write("   - US11167197: Handheld Barbell Jack Tool")
st.write("While many solutions exist, they are not ideal. The barbell jack stand uses a cradle and leverage handle to lift the barbell off the floor so plates can slide on and off. However, barbell jack stands are bulky and expensive. The ramp stand works by having the barbell roll up a slope into a cradle, elevating it ofr plate changes, and then having the plate roll down. The ramp stands are stationary and not portable. The handheld barbell jack is a portable lever tool to prop up the bar, but it requires balancing. None of these ultimately help with picking up and sliding heavy weights onto the bar.")

st.subheader("Dorm chairs rock")
st.write("Problem: Northwestern equips all rooms with a two-position rocking chair (commonly the 'multi-position chair'), intended to serve dual functions as both a study seat and a relaxation seat. However, the chair rocks involuntarily in response to minor weight shifts during focused desk work. This forces users to lose focus trying to think about posture stabilization rather than their study task. Because the chair has no user-controlled mechanism to switch between rocking and locked modes, students cannot adapt it to the task at hand, resulting in reduced focus, poor ergonomic support during study. How might we give Northwestern dorm residents user-controlled switching between rocking and stable seating modes, without replacing the existing chair itself?")
st.write("Prior solutions exist. ")
st.image("dorm_chair_product.png")
st.write("Ergonomics research opposes non-rocking chairs. Dynamic/active seating is associated with improved focus, blood flow, and attention. This means that the current products may not be ideal to help students achieve peak productivity.")
