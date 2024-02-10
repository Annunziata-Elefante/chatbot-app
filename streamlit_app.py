import streamlit as st
from streamlit_timeline import timeline


# ------------------------- PAGE CONFIGURATION -------------------------
st.set_page_config(
    page_title="Annunziata Elefante",
    page_icon="🦋",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# open pdf
pdfFileObj = open('images/resume.pdf', 'rb')

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
    st.page_link("pages/about.py", label="About Me", icon="😸")
    # st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")
    st.divider()
    st.download_button('📝 Download Resume', pdfFileObj, file_name='annunziata_elefante_resume.pdf',mime='pdf')

# ------------------------- PROFILE -------------------------
with st.container():
    # Divide the container into 2 columns
    # col1, col2 = st.columns([1, 3])
    # with col1:
    #     st.image('images/photo_profile.webp')                # caption='Annunziata Elefante'   
    # with col2:
    #     st.header("Hey there. 🦋")
    #     st.header("I'm Annunziata Elefante!")
    #     st.write("I'm a programmer specializing in Data Science and Machine Learning, as well as a freelance Web Developer.")
    st.markdown("<h1 style='text-align: center; color: black;'> Hey there. 🦋 </h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'> I'm Annunziata Elefante! </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'> I'm a programmer specializing in Data Science and Machine Learning, as well as a freelance Web Developer. </p>", unsafe_allow_html=True)
    
# ------------------------- SKILLS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> SKILLS </h2>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3, col4 = st.columns(4)
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

with st.container():
    cl1, cl2, cl3, cl4 = st.columns(4)
    with cl1:
        st.markdown("<h2 style='text-align: center; color: black;'> 📊 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> R </p>", unsafe_allow_html=True)
    with cl2:
        st.markdown("<h2 style='text-align: center; color: black;'> 🖥️ </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> WORDPRESS </p>", unsafe_allow_html=True)
    with cl3:
        st.markdown("<h2 style='text-align: center; color: black;'> 📱 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> Angular, Ionic </p>", unsafe_allow_html=True)
    with cl4:
        st.markdown("<h2 style='text-align: center; color: black;'> 🐘 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> MongoDB </p>", unsafe_allow_html=True)
        
# Divider
st.divider()

# ------------------------- WORK TIMELINE -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> WORK TIMELINE </h2>", unsafe_allow_html=True)
  
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# # Divider
# st.divider()

# # ------------------------- PROJECTS -------------------------
# st.markdown("<h2 style='text-align: center; color: black;'> PROJECTS </h2>", unsafe_allow_html=True)


# Divider
st.divider()

# ------------------------- SOCIAL -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> FOLLOW ME </h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**GitHub**: [@Annunziata-Elefante](https://github.com/Annunziata-Elefante)', icon="🐈‍⬛")
with c2:
    st.info('**LinkedIn**: [@nunzia-elefante](https://www.linkedin.com/in/nunzia-elefante/)', icon="🧰")
with c3:
    st.info('**Instagram**: [@__nunzia______](https://www.instagram.com/__nunzia______/)', icon="📸")

# Divider
st.divider()

# ------------------------- CONTACT ME -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> CONTACT ME </h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.write()
with c2:
    st.info('**E-mail**: nunziaelefante@mail.com', icon="📨")
with c3:
    st.write()

# draw celebratory balloons.
# st.balloons()
