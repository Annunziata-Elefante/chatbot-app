import streamlit as st

st.title("🤖🔊 Echo Bot")
st.info("This chatbot echoes your input.", icon="🔍")

# Sidebar with MENU
with st.sidebar:
  st.write("☰ MENU")
  st.page_link("streamlit_app.py", label="Home", icon="🏡")
  st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
