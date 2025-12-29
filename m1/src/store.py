from dataclasses import dataclass, asdict
import streamlit as st

@dataclass
class Message:
    """
    A message in a chat application

    Attributes:
        role (str): The role of the message sender (e.g., 'user', 'assistant')
        content (str): The content of the message
    """
    role: str
    content: str


class Store:
    """
    A simple in-memory store for application state.
    """

    def __init__(self):
        self.messages = []
    
    def load_from_streamlit(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        self.messages = [
            Message(role = m['role'], content = m['content']) for m in st.session_state.messages
        ]
        
    def save_to_streamlit(self):
        st.session_state.messages = [asdict(m) for m in self.messages]
    
    def add_message(self, role: str, content: str):
        message = Message(role=role, content=content)
        self.messages.append(message)
        self.save_to_streamlit()
    