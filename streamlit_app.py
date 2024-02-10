import streamlit as st


# st.title("🦋Hi, I'm Nunzia!")
# st.write("")
# st.info("Data Science & Machine Learning || University of Fisciano, Italy || Web Developer Freelancer", icon="💻")

# SIDEBAR
with st.sidebar:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('images/profile-modified.png')
    with col2:
        st.header("Annunziata Elefante")
        st.caption("Front-End Developer")
    st.write("☰ MENU")
    st.page_link("streamlit_app.py", label="Home", icon="🏡")
    st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")

# PROFILE
col1, col2 = st.columns(2)
with col1:
    st.image('images/photo_profile.webp')                # caption='Annunziata Elefante'   
with col2:
    st.header("Hey there. 🦋")
    st.header("I'm Annunziata Elefante!")
    st.write("I'm a programmer specializing in Data Science and Machine Learning, as well as a freelance Web Developer.")
     

# draw celebratory balloons.
# st.balloons()
