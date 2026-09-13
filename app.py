from dotenv import load_dotenv
load_dotenv()

from src.langgraph.main import load_langgraph_app

if __name__=="__main__":
    load_langgraph_app()


##  py -m streamlit run app.py 
