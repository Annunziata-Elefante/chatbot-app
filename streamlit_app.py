import streamlit as st
# from langchain.llms import OpenAI

# st.title("Echo Bot")
st.title("🦋Hi, I'm Nunzia!")
#st.write("")
st.info("Application Test", icon="💻")

with st.sidebar:
  st.page_link("streamlit_app.py", label="Home", icon="🏡")
  st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")
