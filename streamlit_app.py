import streamlit as st

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
    col1, col2, col3, col4, col5 = st.columns(4)
    with col1:
        st.markdown("<h2 style='text-align: center; color: black;'> 🐍 </h2>", unsafe_allow_html=True)
        st.markdown("<caption style='text-align: center; color: black;'> PYTHON </caption>", unsafe_allow_html=True)
        # st.subheader("🐍")
        # st.caption("PYTHON")
    with col2:
        st.markdown("<h2 style='text-align: center; color: black;'> ♨️ </h2>", unsafe_allow_html=True)
        # st.subheader("♨️")
        st.caption("JAVA")
    with col3:
        st.markdown("<h2 style='text-align: center; color: black;'> 🌐 </h2>", unsafe_allow_html=True)
        # st.subheader("🌐")
        st.caption("HTML, CSS, JS")
    with col4:
        st.markdown("<h2 style='text-align: center; color: black;'> 🐬 </h2>", unsafe_allow_html=True)
        # st.subheader("🐬")
        st.caption("MySQL")
    

# draw celebratory balloons.
# st.balloons()
