from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools

from agno.playground import Playground, serve_playground_app
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

memoria = Memory(
    model=Gemini(id="gemini-1.5-pro-latest"),
    db = SqliteMemoryDb(table_name="user_memories", db_file="tmp/memory.db"),
)

agente = Agent(
    model = Gemini(id="gemini-1.5-pro-latest"),
    tools = [TavilyTools()],
    memory=memoria,
    enable_agentic_memory= True,
    instructions="Você é um pesquisador e deve responder sempre o usuario de senhor!",
    debug_mode= True,
)



