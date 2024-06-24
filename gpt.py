import os
import openai
import random

class ChatGPT(object):
    def __init__(self):
        self.client = None

    def question(self, q : str):
        response = self.client.chat.completions.create(
        model="gpt-4o",
        temperature=0.8,
        top_p= 0.3,
        seed = int(random.random()),
        messages=[
            {"role": "system", "content": "YYou are ChatGPT, you speak french, answer as concisely as possible"},
            {"role": "user", "content" : f"{q}"},
        ]
        )
        return (response.choices[0].message.content)
    
chatGPT = ChatGPT()