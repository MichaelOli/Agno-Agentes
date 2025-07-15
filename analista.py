from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # Adicione esta linha para registrar a ferramenta com o agente
    tools=[YFinanceTools()], 
    debug_mode=True,
    instructions=(
        "Você é um assistente de pesquisa que pode acessar informações financeiras "
        "e responder perguntas sobre o mercado de ações. Para criptomoedas, use o formato 'BTC-USD'. "
        "Use tabelas para poder mostrar a informação de forma organizada."
    )
)

# Para garantir o sucesso, você pode ser mais explícito no prompt
agente.print_response("Qual o valor atual da ultima cotação do bitcoin (ticker BTC-USD)?", stream=True)