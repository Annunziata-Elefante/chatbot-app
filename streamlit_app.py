import streamlit as st
# import requests
# from streamlit_timeline import st_timeline

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
    col1, col2 = st.columns([1, 4])
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

# ------------------------- WORK TIMELINE -------------------------
# st.markdown("<h2 style='text-align: center; color: black;'> WORK TIMELINE </h2>", unsafe_allow_html=True)

# with st.container():
#     st.markdown("""""")
#     st.subheader('📌 Career Snapshot')

#     # load data
#     # with open('example.json', "r") as f:
#     #     data = f.read()
#     items = [
#     {"Position": "WEB DEVELOPER FREELANCER", "start": "2021", "end": "Today"},
#     {"Position": "RESEARCH FELLOW", "start": "2023-04-03", "end": "2023-11-03"}
# ]
#     # render timeline
#     timeline(items, height=400)
# ------------------------- 

# Divider
st.divider()

# ------------------------- PROJECTS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> PROJECTS </h2>", unsafe_allow_html=True)


# ------------------------- CONTACT ME -------------------------
# st.markdown("<h2 style='text-align: center; color: black;'> CONTACT ME </h2>", unsafe_allow_html=True)
# with col2:
#         email = info["Email"]
#         contact_form = f"""
#         <form action="<https://formsubmit.co/{email}>" method="POST">
#             <input type="hidden" name="_captcha value="false">
#             <input type="text" name="name" placeholder="Your name" required>
#             <input type="email" name="email" placeholder="Your email" required>
#             <textarea name="message" placeholder="Your message here" required></textarea>
#             <button type="submit">Send</button>
#         </form>
#         """
#         st.markdown(contact_form, unsafe_allow_html=True)


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
# draw celebratory balloons.
# st.balloons()
