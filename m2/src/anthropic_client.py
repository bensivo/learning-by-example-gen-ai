import requests
from store import Message

class AnthropicClient:
    """
    Client for interacting with the Anthropic API.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def send_message(
        self, 
        messages: list[Message], 
        system_prompt: str = "",
        model: str = 'claude-sonnet-4-5-20250929', 
        max_tokens: int = 1024
    ) -> str:
        """
        Send a message to the Anthropic API and return the response.
        """
        response = requests.post(
            url='https://api.anthropic.com/v1/messages',
            headers={
                'x-api-key': self.api_key,
                'content-type': 'application/json',
                'anthropic-version': '2023-06-01'
            },
            json={
                'model': model,
                'max_tokens': max_tokens,
                'messages': [ {
                    'role': m.role,
                    'content': m.content
                } for m in messages],
                'system': system_prompt
            }
        )
        data = response.json()
        return data