from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
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

agente = Agent(
    model=Groq(id ="llama-3.3-70b-versatile"),
    tools=[TavilyTools(),celcius_para_fahrenheit],
    debug_mode=True
    )

agente.print_response("Use suas ferramentas para responder a temperatura de hoje em brasilia convertida para Fahrenheit")