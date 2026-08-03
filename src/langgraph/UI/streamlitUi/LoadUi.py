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

        # for fetch news button before the user message input box
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        ## left side portion of the page for user controls
        with st.sidebar:

            llms_options = self.config.get_llms_options()## from src.langgraph.UI.uiconfigfile.py
            usecases_options = self.config.get_usecases_options() ## from src.langgraph.UI.uiconfigfile.py

            # LLM selection dropdown
            self.user_controls["selected_llm"] = st.selectbox("Select LLM:", llms_options)

            if self.user_controls["selected_llm"] == 'Groq':

                models_options = self.config.get_groq_models_options() ## from src.langgraph.UI.uiconfigfile.py   

                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model:", models_options)

                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]= st.text_input("Enter your Groq API Key:", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to proceed.")


            # Use case selection dropdown
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecases_options)

            if self.user_controls["selected_usecase"] == 'Chatbot With Tools' or self.user_controls["selected_usecase"] == 'AI News':
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"]= st.text_input("Enter your Tavily API Key:", type="password")            
                # validation for Tavily API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API Key to proceed.")

            if self.user_controls["selected_usecase"] == 'AI News':
                st.subheader("AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox("Select Time Frame", ["Daily", "Last 7 days", "Last 30 days"], index=0)

                if st.button("Fetch AI News", use_container_width=True):
                   st.session_state.isFetchButtonClicked = True
                   st.session_state.time_frame = time_frame

        return self.user_controls
