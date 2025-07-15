from agno.agent import Agent
from agno.playground import Playground, serve_playground_app
from agno.storage.sqlite import SqliteStorage
#from agno.models.groq import Groq
from agno.models.google import Gemini
from agno.embedder.google import GeminiEmbedder

#Informando a base de conhecimento do agente
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb

from dotenv import load_dotenv
load_dotenv()

embedder = GeminiEmbedder(id="models/embedding-001")

vetor_db = ChromaDb(
    collection="pdf_agentes_gemini", path="tmp/chromadb", embedder=embedder)

knowledge = PDFKnowledgeBase(
    path = "readme.pdf",
    vector_db=vetor_db,
    reader=PDFReader(chunk=True)
)
print("Gerando embeddings com o Google Gemini...")
knowledge.load()
print(" Embeddings gerados com sucesso!")

db = SqliteStorage(
    db_file="tmp/agente.db",
    table_name="agente_history"
)

agente = Agent(
    name = 'Agente de PDFs',
    description = 'Agente que utiliza ferramentas para responder perguntas sobre PDFs',
    #model=OpenAIChat(id ="gpt-4.1-mini"),
    model=Gemini(id="gemini-1.5-pro-latest"),
    add_history_to_messages=True,
    num_history_runs=3,
    knowledge=knowledge,
    storage=db
    #debug_mode=True
)

aplicacao = Playground(
    agents=[agente]
).get_app()

if __name__ == "__main__":
    serve_playground_app("pdf_agente:aplicacao", reload=True)