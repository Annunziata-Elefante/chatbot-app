import streamlit as st
# from langchain.llms import OpenAI

# st.title("Echo Bot")
st.title("🦋Hi, I'm Nunzia!")
#st.write("")
st.info("Application Test", icon="💻")

siderbar_list = st.page_link("streamlit_app.py", label="Home", icon="🏡")
siderbar_list = st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")
