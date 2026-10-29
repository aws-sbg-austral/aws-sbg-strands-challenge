import sys
from pathlib import Path
from urllib.parse import urlparse

from mcp import StdioServerParameters, stdio_client
from strands import Agent, tool
from strands.hooks import BeforeToolCallEvent
from strands.models.ollama import OllamaModel
from strands.tools.mcp import MCPClient
from strands.vended_plugins.skills import AgentSkills

CARPETA = Path(__file__).parent
SITIOS_PERMITIDOS = {"strandsagents.com", "es.wikipedia.org"}


@tool
def contar_palabras(texto: str) -> int:
    """Cuenta cuántas palabras tiene un texto.

    Args:
        texto: El texto a analizar.
    """
    return len(texto.split())


# Hook de guardrail: antes de cada tool, si el agente quiere leer una página
# que no está en SITIOS_PERMITIDOS, se cancela la llamada.
def solo_sitios_permitidos(event: BeforeToolCallEvent) -> None:
    if event.tool_use["name"] != "fetch":
        return
    sitio = urlparse(str(event.tool_use["input"].get("url", ""))).hostname
    if sitio not in SITIOS_PERMITIDOS:
        event.cancel_tool = f"Bloqueado por el guardrail: {sitio} no está en los sitios permitidos."


# MCP de fetch: le suma al agente una tool `fetch` para leer páginas web.
# El server corre local con el mismo Python (está en requirements.txt).
fetch_mcp = MCPClient(
    lambda: stdio_client(StdioServerParameters(command=sys.executable, args=["-m", "mcp_server_fetch"]))
)

agent = Agent(
    model=OllamaModel(host="http://localhost:11434", model_id="llama3.2"),
    system_prompt="Sos un asistente que responde en español rioplatense.",
    tools=[contar_palabras, fetch_mcp],
    plugins=[AgentSkills(skills=[CARPETA / "skills"])],
    hooks=[solo_sitios_permitidos],
)

if __name__ == "__main__":
    print("Pedile algo al agente (Enter vacío para salir). Por ejemplo:")
    print('  ¿La frase "hoy aprendí a crear agentes con Strands" entra en un límite de 5 palabras?')
    print("  ¿De qué trata https://strandsagents.com?")
    print("  Leé https://example.com y resumila  (el guardrail la bloquea)")
    while pedido := input("\n> ").strip():
        agent(pedido)
