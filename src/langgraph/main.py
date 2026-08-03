import streamlit as st

from src.langgraph.UI.streamlitUi.LoadUi import LoadStreamlitUi
from src.langgraph.llms.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.UI.streamlitUi.display_results import DisplayResultStreamlit

def load_langgraph_app():

    """ Loads and runs the LangGraph AgenticAI application with Streamlit UI.

        This function initializes the UI, handles user input, configures the LLM model,

        sets up the graph based on the selected use case, 

        and displays the output while implementing exception handling for robustness. 
    """

    ui = LoadStreamlitUi() ## Load the Streamlit UI
    user_input = ui.load_ui() ## Load the user controls from the UI

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    ## default ==>>>> user_message = st.chat_input("Enter your message:")
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")


    if user_message:
        try: 
            ##================== model=================
            obj_llm_config = GroqLLM(user_controls_input = user_input) ## Configure the LLM model based on user input
            model = obj_llm_config.get_llm_model() ## Configure the model

            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            ##================== useCase =================
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return

            ##================== graph Builder  =================
            graph_builder = GraphBuilder(model)
            try: 
                graph = graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

            except Exception as e :
                st.error(f"Error: graph set up faiild - {e} ")
                return

        except Exception as e:
            st.error(f"Error configuring the LLM model: {e}")
            return  
    