import streamlit as st

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
    st.divider()
    st.download_button('📝 Download Resume', pdfFileObj, file_name='annunziata_elefante_resume.pdf',mime='pdf')

# ------------------------- ABOUT ME -------------------------
# st.markdown("<h2 style='text-align: center; color: black;'> ABOUT ME 🌼 </h2>", unsafe_allow_html=True)
with st.container():
    # Divide the container into 2 columns
    # col1, col2 = st.columns([1, 3])
    # with col1:
    #     st.image('images/memoji.webp')                # caption='Annunziata Elefante'   
    # with col2:
    #     st.write("I'm Nunzia!. \nI'm 25 years-old and I'm a front-end developer based in Italy. I'm specialized in Data Science & Machine Learning🤖 and during this peroid I'm workis as a Web Developer Freelancer.\n <ypu should also know that I'm also a passionate and creative girl who loves spending time with loved ones and cats😸.\nI'm always availble for a chat ot coffee☕")
    # Divide the container into 2 columns
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image('images/memoji.webp')                # caption='Annunziata Elefante'   
    with col2:
        st.header("I'm Nunzia!")
        st.write("I'm 25 years-old and I'm a front-end developer based in Italy. I'm specialized in Data Science & Machine Learning🤖 and during this peroid I'm workis as a Web Developer Freelancer.")
        st.write("You should also know that I'm also a passionate and creative girl who loves spending time with loved ones and cats😸.\nI'm always availble for a chat ot coffee☕")

# st.divider()

# ------------------------- EDUCATION -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> EDUCATION 🎓 </h2>", unsafe_allow_html=True)
with st.container():
    cl1, cl2 = st.columns([1, 3])
    with cl1:
        st.caption("2021 - 2023")
    with cl2:
        st.subheader("MASTER'S DEGREE IN COMPUTER SCIENCE (LM-18)")
        st.write("University of Salerno \nTHESIS: 'Inference of Sensitive Information in Intelligent Environments through the Analysis of Trigger-Action Rules.' \nFINAL GRADE: 110/110 cum laude")
    st.divider()
    c1, c2 = st.columns([1, 3])
    with c1:
        st.caption("2021 - 2023")
    with c2:
        st.subheader("BACHELOR'S DEGREE IN COMPUTER SCIENCE (L-31)")
        st.write("University of Salerno \nTHESIS: 'Development of front-end services for the EcoGrowth application.' \nFINAL GRADE: 110/110 cum laude")
