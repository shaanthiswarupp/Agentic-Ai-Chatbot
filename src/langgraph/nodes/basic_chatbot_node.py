from src.langgraph.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        messages = state["messages"]
        response = self.llm.invoke(messages)
        return {"messages": [response]}
        
        #return {"messages":self.llm.invoke(state['messages'])} ----------------> old 1 line 

