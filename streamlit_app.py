import streamlit as st


st.title("🦋Hi, I'm Nunzia!")
# st.write("")
st.info("Data Science & Machine Learning || University of Fisciano, Italy || Web Developer Freelancer", icon="💻")

with col1:
    st.image('iamges/memoji.webp', caption='Sunrise by the mountains')

# Controls whether the default sidebar page navigation in a multipage app is displayed.
# Default: true
showSidebarNavigation = true

# Sidebar for MENU
with st.sidebar:
    st.write("☰ MENU")
    st.page_link("streamlit_app.py", label="Home", icon="🏡")
    st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")

# draw celebratory balloons.
st.balloons()
