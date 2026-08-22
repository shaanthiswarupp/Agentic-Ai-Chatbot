import os
import streamlit as st

import groq
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class LLMFactory:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        provider = self.user_controls_input.get("selected_llm")

        try:
            if provider == "Groq":
                groq_api_key = self.user_controls_input["GROQ_API_KEY"]
                selected_groq_model=self.user_controls_input["selected_groq_model"]

                if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                    st.error("Please Enter the Groq API KEY")

                llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
                
            elif provider == "OpenAI":
                openai_api_key = self.user_controls_input["OPENAI_API_KEY"]
                selected_openai_model = self.user_controls_input["selected_openai_model"]

                if openai_api_key == '' and os.environ["OPENAI_API_KEY"] == '':
                    st.error("Please Enter the OpenAI API KEY")

                llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)

        except Exception as e:
            raise ValueError(f"Error Occured with {e}")
        return llm

       