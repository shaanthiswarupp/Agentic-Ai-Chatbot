from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode

from src.langgraph.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode

from src.langgraph.nodes.chatbot_with_tool_node import ChatbotWithToolNode




class GraphBuilder:
    ## ============ Constructor to initialize the GraphBuilder
    def __init__(self, model):        
        self.llm = model
        self.graph_builder = StateGraph(State)



    # ================= for chatbot =============
    def basic_chatbot_build_graph(self):
        """ Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.    """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node( "chatbot", self.basic_chatbot_node.process )
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)



    #=========== for chatbot with web    tools ==========================================================
    def chatbot_with_tool_build_graph(self):
        """  Builds a chatbot with web graph tool integration.
          This method creates a chatbot graph includs the both BasicChatbotNode and a tool node . 
             it defines tools , initializes the chatbot with tool capabilities, and  sets up conditonal and direct edges between nodes.
        the chatbot is set as the entry point  """
        
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # === llm with tools integration
        llm= self.llm

        #======= define the chatbot with tool node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        
        # add node 
        self.graph_builder.add_node("chatbot", chatbot_node )# from nodes 
        self.graph_builder.add_node("tools", tool_node)

        # add edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        



    ## ============== main function to setup the graph based on the usecase selected by the user in the UI ==========================
    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()


        elif usecase == "Chatbot With Tools":
            self.chatbot_with_tool_build_graph()

        return self.graph_builder.compile()
