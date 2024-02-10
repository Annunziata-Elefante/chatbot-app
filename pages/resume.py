import streamlit as st
import base64
from constant import *

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
# local_css("style/style.css")

# st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)
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
    st.page_link("pages/resume.py", label="Resume", icon="📝")
    st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")
    st.divider()
    st.download_button('Download Resume', pdfFileObj, file_name='annunziata_elefante_resume.pdf',mime='pdf')


# ------------------------- RESUME -------------------------
st.title("📝 Resume")

pdfFileObj = open('images/resume.pdf', 'rb')
st.download_button('Download Resume', pdfFileObj, file_name='annunziata_elefante_resume.pdf',mime='pdf')
st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open("images/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
