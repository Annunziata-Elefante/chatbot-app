import streamlit as st

# st.title("Echo Bot")
st.title("🦋Hi, I'm Nunzia!")
#st.write("")
st.info("Data Science & Machine Learning || University of Fisciano, Italy || Web Developer Freelancer", icon="💻")

# Controls whether the default sidebar page navigation in a multipage app is
# displayed.
# Default: true
showSidebarNavigation = true

# Sidebar with MENU
with st.sidebar:
  st.page_link("streamlit_app.py", label="Home", icon="🏡")
  st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")

# draw celebratory balloons.
st.balloons()
