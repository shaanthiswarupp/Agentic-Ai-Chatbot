from src.langgraph.state.state import State

class ChatbotWithToolNode:
    """ Chatbot logic enhanced with tool integration """

    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """ Processes the input state and generates a response with tool integration. """

        user_input = state["messages"][-1] if state["messages"] else ""  # Get the last user message

        llm_response = self.llm.invoke( [ { "role": "user",  "content": user_input } ] )  # Generate response using the LLM


        tool_response =  f"Tool Integration for: {user_input} " # Get the tool response if available

        return {"messages": [ {"role": "assistant", "content": llm_response}, {"role": "tool", "content": tool_response} ] }


    def create_chatbot(self, tools):
        """ returns a chatbot node function """

        llm_with_tools = self.llm.bind_tools(tools)  # Bind the tools to the LLM

        def chatbot_node(state: State):
            """  Chatbot logic for processing the input state and returning a response """
            return {"messages": [llm_with_tools.invoke(state["messages"])] }
        
        return  chatbot_node





        

