# M1 - Chat interface

This modules implements a basic chat interface using the Anthropic Claude APIs, and streamlit as a UI layer.

Features of this module include:
- Basic question-answer chat
- Writing help, task help, summarization, etc. (anything a basic LLM can do)


Things this module CANT do:
- Act without being prompted
- Inject documents
- Use external resources on its own

## Running
```
uv sync
uv run streamlit run src/main.py
```