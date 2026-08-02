from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """ Returns a list of tools to be used in the chatbot . """
    tools=[ TavilySearchResults(max_results=2) ] 
    return tools

def create_tool_node(tools):
    """ Creates a ToolNode for the  graph. """
    tool_node = ToolNode(tools=tools)
    return tool_node