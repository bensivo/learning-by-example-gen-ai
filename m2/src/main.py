import streamlit as st
from store import Store, Message
from anthropic_client import AnthropicClient
from system_prompt import generate_system_prompt
import os

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

anthropic_client = AnthropicClient(api_key=ANTHROPIC_API_KEY)

store = Store()
store.load_from_streamlit()

st.title("M1: Basic Chat")

with st.sidebar:
    verbosity_select = st.radio("Verbosity", options=["low", "medium", "high"], index=1)
    tone_select = st.radio("Tone", options=["casual", "professional", "academic"], index=2)

# Render chat message history
for message in store.messages:
    if message.role == 'user':
        with st.chat_message("user"):
            st.write(message.content)
            continue

    if message.role == 'assistant':
        with st.chat_message("assistant"):
            st.write(message.content)
            continue

# Handle new user input
input = st.chat_input("Hello!")
if input:
    # Add message to state, so it's there on refresh
    # But also write it to the screen immediately
    store.add_message(role='user', content=input)
    with st.chat_message("user"):
        st.write(input)

    # Display a '...' for now while we call the API,
    # Once the API responds, add the response to state, then rerender to replace the '...' with the real message
    with st.chat_message("assistant"):
        st.write("...")

        system_prompt = generate_system_prompt(verbosity_select, tone_select) 

        res = anthropic_client.send_message(
            messages = [ Message(role=m.role, content=m.content) for m in store.messages ], 
            system_prompt = system_prompt
        )

        for message in res['content']:
            store.add_message(
                role='assistant',
                content=message['text']
            )

        st.rerun()