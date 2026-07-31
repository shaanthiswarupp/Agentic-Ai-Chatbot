import os
import streamlit as st
from src.langgraph.UI.uiconfigfile import config

## Streamlit is an open-source Python framework that allows you to 
# turn Python scripts into interactive web applications 
# without writing HTML, CSS, or JavaScript. It’s widely used for data visualization 

class LoadStreamlitUi:
    def __init__(self):
        self.config = config()
        self.user_controls = {} ## store data from user controls in a dictionary


    def load_ui(self):
        ## Set the page title and layout from src.langgraph.UI.uiconfigfile.py

        st.set_page_config( page_title = "🤖 " + self.config.get_page_title(), layout="wide" )
        st.header("🤖 " + self.config.get_page_title()) ## page title from src.langgraph.UI.uiconfigfile.py

        ## left side portion of the page for user controls
        with st.sidebar:

            llms_options = self.config.get_llms_options()## from src.langgraph.UI.uiconfigfile.py
            usecases_options = self.config.get_usecases_options() ## from src.langgraph.UI.uiconfigfile.py

            # LLM selection dropdown
            self.user_controls["selected_llm"] = st.selectbox("Select LLM:", llms_options)

            if self.user_controls["selected_llm"] == 'groq':
                models_options = self.config.get_groq_models_options() ## from src.langgraph.UI.uiconfigfile.py
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model:", models_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]= st.text_input("Enter your Groq API Key:", type="password")
                
            

            # Use case selection dropdown
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case:", usecases_options)
            
        return self.user_controls
