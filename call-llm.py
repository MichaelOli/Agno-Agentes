from agno.models.groq import Groq
from agno.models.message import Message

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")
msg = Message(
    role="user",
    content=([{"type": "text", "text": "Olá meu nome é Michael Ribeiro, sou um desenvolvedor de software e estou aprendendo a usar o Groq com Python."}])
    )

response = model.invoke([msg])
respotas = print(response.choices[0].message.content)