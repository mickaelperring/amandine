import os
import openai
import random
import streamlit as st
import os

class ChatGPT(object):
    def __init__(self):
        apiKey = st.secrets["API_KEY"]
        self.client = openai.OpenAI(api_key = apiKey)

    def question(self, q : str):
        response = self.client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.6,
        top_p= 0.85,
        seed = int(random.random()),
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are ChatGPT, you speak french, answer as concisely as possible"},
            {"role": "user", "content" : f"{q}"},
        ]
        )
        return (response.choices[0].message.content)
    
chatGPT = ChatGPT()