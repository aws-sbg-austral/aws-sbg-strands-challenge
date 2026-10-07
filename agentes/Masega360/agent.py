from strands import Agent, tool
from strands.models.ollama import OllamaModel


@tool
def contar_palabras(texto: str) -> int:
    """Cuenta cuántas palabras tiene un texto.

    Args:
        texto: El texto a analizar.
    """
    return len(texto.split())


agent = Agent(
    model=OllamaModel(host="http://localhost:11434", model_id="llama3.2"),
    system_prompt="Sos un asistente que responde en español rioplatense.",
    tools=[contar_palabras],
)

if __name__ == "__main__":
    agent("¿Cuántas palabras tiene la frase 'hoy aprendí a crear agentes con Strands'?")
