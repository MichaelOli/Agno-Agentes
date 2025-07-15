from agno.agent import Agent
from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from agno.embedder.google import GoogleAIEmbedder 
from agno.tools.tavily import TavilyTools
from agno.storage.sqlite import SQLiteStorage
from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv
load_dotenv()

def celcius_para_fahrenheit(celsius: float):
    """
    Converte Celsius para Fahrenheit. 
    Args: 
        celsius (float): Temperatura em Celsius.
    Returns:
        float: Temperatura convertida em Fahrenheit.
    """
    return (celsius * 9/5) + 32

db = SQLiteStorage(
    db_path="playground.db",
    table_name="playground_history"
)

agente = Agent(
    name = 'Agente de Pesquisa',
    description = 'Agente que utiliza ferramentas para responder perguntas sobre o clima e outras informações',
    #model=OpenAIChat(id ="gpt-4.1-mini"),
    model=Groq(id ="llama-3.3-70b-versatile"),
    tools=[TavilyTools(),celcius_para_fahrenheit],
    add_history_to_messages=True,
    num_history_runs=3,
    storage=db,
    debug_mode=True
)

aplicacao = Playground(
    agents=[agente]
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:aplicacao", reload=True)

#agente.print_response("Use suas ferramentas para responder a temperatura de hoje em brasilia convertida para Fahrenheit")