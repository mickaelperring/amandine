import streamlit as st

class DictWrapper(object):

    d : dict

    def __init__(self, d):
        object.__setattr__(self, 'd', d)
        
    def __getattr__(self, key):
        return self.d[key]
   
    def __setattr__(self, key, value):
        self.d[key] = value

    def init(self, key, value):
        if not key in self.d:
            self.d[key] = value

G = DictWrapper(st.session_state)