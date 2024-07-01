import streamlit as st

from utils import generate_response

# App title
st.title("Simple ChatBot")

# Hugging Face Credentials
with st.sidebar:
    st.title("Login HugChat")
    hf_email = st.text_input("Enter E-mail:")
    hf_pass = st.text_input("Enter Password:", type="password")
    if not (hf_email and hf_pass):
        st.warning("Please enter your account!", icon="⚠️")
    else:
        st.success("Proceed to entering your prompt message!", icon="👉")


# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
