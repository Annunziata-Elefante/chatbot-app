import streamlit as st


st.title("🦋Hi, I'm Nunzia!")
# st.write("")
st.info("Data Science & Machine Learning || University of Fisciano, Italy || Web Developer Freelancer", icon="💻")

col1, col2 = st.columns(2)
with col1:
    st.image('images/memoji.webp', caption='Nunzia')

# Sidebar for MENU
'''
with st.sidebar:
    st.write("☰ MENU")
    st.page_link("streamlit_app.py", label="Home", icon="🏡")
    st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")
''''

# draw celebratory balloons.
st.balloons()
