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
        st.write("I'm 25 years-old and I'm a front-end developer based in Italy. I'm specialized in Data Science & Machine Learning🤖 and during this peroid I'm workis as a Web Developer Freelancer💻.")
        st.write("You should also know that I'm also a passionate and creative girl who loves spending time with loved ones❤️ and cats😸.\nI'm always availble for a chat ot coffee☕")

st.divider()

# ------------------------- EDUCATION -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> EDUCATION 🎓 </h2>", unsafe_allow_html=True)
with st.container():
    cl1, cl2 = st.columns([1, 3])
    with cl1:
        st.caption("2021 - 2023")
    with cl2:
        st.write("MASTER'S DEGREE IN COMPUTER SCIENCE (LM-18)")
        st.write("_University of Salerno_ \nTHESIS: '_Inference of Sensitive Information in Intelligent Environments through the Analysis of Trigger-Action Rules._' \nFINAL GRADE: 110/110 cum laude")
        
    st.markdown("<p style='text-align: center; color: black;'> 󠀾 </p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 3])
    with c1:
        st.caption("2017 - 2021")
    with c2:
        st.write("BACHELOR'S DEGREE IN COMPUTER SCIENCE (L-31)")
        st.write("_University of Salerno_ \nTHESIS: '_Inference of Sensitive Information in Intelligent Environments through the Analysis of Trigger-Action Rules._' \nFINAL GRADE: 110/110 cum laude")        

st.divider()

# ------------------------- LANGUAGE SKILLS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> LANGUAGE SKILLS 💬 </h2>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center; color: black;'> 🍕 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> Italian - Native language </p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h2 style='text-align: center; color: black;'> 💂 </h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: black;'> English Level C1 - LanguageCert Level 2 Certificate in ESOL International </p>", unsafe_allow_html=True)

st.divider()

# ------------------------- RESEARCH PAPERS -------------------------
st.markdown("<h2 style='text-align: center; color: black;'> RESEARCH PAPERS 📑 </h2>", unsafe_allow_html=True)
# with st.container():
#     cl1, cl2 = st.columns([1, 3])
#     with cl1:
#         st.caption("[4]")
#     with cl2:
#         st.write("B. Breve, G. Cimino, V. Deufemia, A. Elefante, '_Unleashing the Power of NLP Models for Semantic Consistency Checking of Automation Rules_', \nProceedings of the Journal of Visual Language and Computing (JVLC) Vol. 2023 No.2, December 2023, pp.1-14")
            
#     c1, c2 = st.columns([1, 3])
#     with c1:
#         st.caption("[3]")
#     with c2:
#         st.write("B. Breve, G. Cimino, V. Deufemia, A. Elefante, '_A BERT-based Model for Semantic Consistency Checking of Automation Rules_', Proceedings of 29th International DMS Conference on Visualization and Visual Languages (DMSVIVA 2023), San Francisco, 29-30 June, 2023, pp. 87-93, ISSN: 2326-3261")
    
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.caption("[2]")
#     with col2:
#         st.write("B. Breve, G. Cimino, V. Deufemia, A. Elefante, '_User Perception of Risks Associated with IFTTT Applets: A Preliminary User Study_', Proceedings of the Italian Conference on Cybersecurity (ITASEC2023), Bari, 2-5 May, 2023, to appear in CEUR Workshop Proceedings, pp. 1-12")
        
#     col3, col4 = st.columns([1, 3])
#     with col3:
#         st.caption("[1]")
#     with col4:
#         st.write("B. Breve, G. Cimino, G. Desolda, V. Deufemia, A. Elefante, '_On the User Perception of Security Risks of Trigger-Action Rules: A User Study_', Proceedings of the 9th International Symposium on End-User Development (IS-EUD 2023). Cagliari, 6-8 June, 2023, Lecture Notes in Computer Science (LNCS) 13917, 2023, Lucio Davide Spano et al. (Eds.), pp. 162–179, Springer-Verlag")
