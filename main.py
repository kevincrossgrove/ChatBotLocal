# Creating a Virtual Environment Guide
# 1 - python3 -m venv .venv - This creates a virtual environment in the current directory
#     Make sure you choose "Yes" to VS Code popup asking if you want to use the virtual environment
#     If not, you can switch to the virtual enviroment by changing the version of python in the bottom of VS Code.
#     I believe you can also active the venv by typing "source venv/bin/activate" in the terminal
# 2 - Close and reopen VS Code Terminal if needed
# 3 - Create requirements.txt file - touch requirements.txt
# 4 - Update requirements.txt file anytime using: pip freeze > requirements.txt

import streamlit as st
from ollama import Client

# Ollama must be running for this application to work
# ollama run `model_name` starts a server at http://localhost:11434
client = Client(host='http://localhost:11434')

# Set model here!
model='llama3.1'

# Set page title
st.set_page_config(page_title="Local Chat Bot")

# Chatting with Ollama Server
def chat_with_ai(messages):
    stream = client.chat( model=model, messages=messages, stream=True)

    for chunk in stream:
        yield chunk['message']['content']
        

st.header("Local Chat Bot")

# Reduces the padding at the top of the page
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2.5rem;
                }
        </style>
        """, unsafe_allow_html=True)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

 # React to user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message in chat message container
    with st.chat_message("user"):
         st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(chat_with_ai(st.session_state.messages))

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})