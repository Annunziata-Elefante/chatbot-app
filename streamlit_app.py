import streamlit as st
from streamlit_timeline import st_timeline
import streamlit.components.v1 as components

# ------------------------- SIDEBAR -------------------------
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

# ------------------------- PROFILE -------------------------
with st.container():
    # Divide the container into 2 columns
    col1, col2 = st.columns(2)
    with col1:
        st.image('images/photo_profile.webp')                # caption='Annunziata Elefante'   
    with col2:
        st.header("Hey there. 🦋")
        st.header("I'm Annunziata Elefante!")
        st.write("I'm a programmer specializing in Data Science and Machine Learning, as well as a freelance Web Developer.")

# ------------------------- SKILLS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> SKILLS </h2>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("<h2 style='text-align: center; color: black;'> 🐍 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> PYTHON </p>", unsafe_allow_html=True)
        # st.subheader("🐍")
        # st.caption("PYTHON")
    with col2:
        st.markdown("<h2 style='text-align: center; color: black;'> ♨️ </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> JAVA </p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<h2 style='text-align: center; color: black;'> 🌐 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> HTML, CSS, JS </p>", unsafe_allow_html=True)
    with col4:
        st.markdown("<h2 style='text-align: center; color: black;'> 🐬 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> MySQL </p>", unsafe_allow_html=True)
    with col5:
        st.markdown("<h2 style='text-align: center; color: black;'> 🖥️ </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> WORDPRESS </p>", unsafe_allow_html=True)

# ------------------------- PROJECTS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> WORK TIMELINE </h2>", unsafe_allow_html=True)

with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    # with open('example.json', "r") as f:
    #     data = f.read()
    items = [
    {"Position": "WEB DEVELOPER FREELANCER", "start": "2021", "end": "Today"},
    {"Position": "RESEARCH FELLOW", "start": "2023-04-03", "end": "2023-11-03"}
]
    # render timeline
    timeline(items, height=400)
# timeline = st_timeline(items, groups=[], options={}, height="300px")
# st.subheader("Selected item")
# st.subheader(timeline)


# draw celebratory balloons.
# st.balloons()
