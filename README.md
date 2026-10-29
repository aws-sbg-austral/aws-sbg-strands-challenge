# Strands Challenge 🧵

Challenge del **AWS Student Builder Group – Universidad Austral**.

Ya viste cómo funciona [Strands Agents](https://strandsagents.com): cómo crear un agente, invocarlo y darle tools. Y en *Bitácoras Agénticas · Episodio 1* viste cómo equiparlo con hooks, MCPs y skills. Ahora te toca a vos.

## La consigna

Creá un agente que **resuelva un problema real de tu día a día**.

Requisitos:

1. Hacé un **fork** de este repo y trabajá en tu fork.
2. Tu agente tiene que estar hecho **sí o sí con Strands Agents**. No vale otro framework (LangChain, CrewAI, etc.).
3. Tiene que tener **al menos una tool custom** definida por vos con `@tool`.
4. Tiene que tener **al menos un hook de guardrail**: un hook que frene algo que tu agente no debería hacer nunca (por ejemplo, cancelar una tool con `event.cancel_tool`).
5. Entregalo abriendo un **Pull Request** a este repo (ver [Cómo entregar](#cómo-entregar)).

**Suman puntos** (uno, el otro o los dos):

- **MCP**: conectá al menos un servidor MCP con `MCPClient`.
- **Skills**: empaquetá instrucciones en una skill (`SKILL.md`) y cargala con `AgentSkills`.

Ideas para arrancar: dividir gastos con amigos, armar la lista del súper, organizar tu semana de parciales, recomendarte qué cocinar con lo que tenés en la heladera, avisarte qué bondi te conviene... lo que te sirva a vos.

## Cómo arrancar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r agentes/Masega360/requirements.txt
python agentes/Masega360/agent.py
```

[`agentes/Masega360/`](agentes/Masega360/) es un ejemplo mínimo con una tool (`contar_palabras`), un hook de guardrail, un MCP, una skill y el formato de entrega.

> 💡 Es un ejemplo bobo a propósito, solo para que veas la estructura. **Esperamos cosas mucho más copadas**: algo que de verdad uses, con tools que hagan algo interesante.

### Modelo

El ejemplo corre **local con [Ollama](https://ollama.com)**, gratis y sin cuenta de nada. Antes de correrlo:

```bash
ollama pull llama3.2
```

Podés usar cualquier modelo de Ollama que soporte tools (por ejemplo `qwen3` o `llama3.1`): cambiá el `model_id` en `agent.py`.

**¿Preferís Claude en Amazon Bedrock?** Sacá el `model=...` del `Agent` y Strands usa Bedrock por defecto. Necesitás:

- Credenciales de AWS (`aws login` o `aws configure`).
- `botocore[crt]` instalado si te logueaste con `aws login`.
- Si tu cuenta es nueva, completar el formulario de uso de modelos de Anthropic en la consola de Bedrock (se hace una sola vez).

Para otros proveedores, mirá *Model Providers* en la [doc de Strands](https://strandsagents.com). Sea cual sea el modelo, el agente tiene que ser de Strands.

## Recordatorio rápido

```python
from strands import Agent, tool

@tool
def mi_tool(param: str) -> str:
    """Qué hace la tool. El agente lee este docstring para decidir cuándo usarla.

    Args:
        param: Qué es este parámetro.
    """
    return ...

agent = Agent(tools=[mi_tool])
agent("Pedile algo")
```

- El **docstring** y los **type hints** son lo que el modelo ve: escribilos bien.
- Podés sumar tools ya hechas con `pip install strands-agents-tools`.

### Hook de guardrail

Se ejecuta antes de cada tool. Si setea `event.cancel_tool`, la tool no corre y el agente recibe ese mensaje como error.

```python
from strands.hooks import BeforeToolCallEvent

def no_borrar(event: BeforeToolCallEvent) -> None:
    if event.tool_use["name"] == "borrar_archivo":
        event.cancel_tool = "Bloqueado: este agente no borra archivos."

agent = Agent(tools=[...], hooks=[no_borrar])
```

### MCP

Conectar un servidor MCP es configuración, no código: sus tools se suman a las tuyas.

```python
from mcp import StdioServerParameters, stdio_client
from strands.tools.mcp import MCPClient

fetch_mcp = MCPClient(lambda: stdio_client(
    StdioServerParameters(command="uvx", args=["mcp-server-fetch"])
))

agent = Agent(tools=[mi_tool, fetch_mcp])
```

### Skills

Una skill es una carpeta con un `SKILL.md`: un *frontmatter* con `name` y `description`, y abajo las instrucciones. El agente ve la descripción y carga las instrucciones solo cuando las necesita.

```python
from strands.vended_plugins.skills import AgentSkills

agent = Agent(tools=[mi_tool], plugins=[AgentSkills(skills=["./skills"])])
```

> Con modelos chicos de Ollama, muchas tools juntas confunden. Si tu agente usa un MCP con varias tools, probá con `qwen3` o con Claude en Bedrock.

## Cómo entregar

1. En tu fork, duplicá la carpeta [`agentes/tu_nombre/`](agentes/tu_nombre/) con el nombre de tu usuario de GitHub (no la renombres: la plantilla tiene que quedar) y poné ahí todo lo tuyo:
   ```
   agentes/
   └── tu-usuario/
       ├── agent.py
       ├── README.md
       ├── requirements.txt   # strands-agents[ollama] + cualquier librería extra que uses
       └── skills/            # opcional, si usás skills
   ```
   No toques archivos fuera de tu carpeta, así no hay conflictos con los demás.
2. Completá el `README.md` de tu carpeta (tenés uno de ejemplo en [`agentes/Masega360/`](agentes/Masega360/)):
   - **Nombre** del agente
   - **Problema** que resuelve
   - **Tools custom** que definiste y qué hace cada una
   - **Guardrail**: qué frena tu hook y por qué
   - **MCP y skills**, si usaste
   - **Cómo correrlo**
3. Abrí un **Pull Request** desde tu fork a `main` de este repo, con el título `[Challenge] <nombre de tu agente>`.

> ⚠️ Nunca subas credenciales (keys de AWS, tokens, `.env`). Usá variables de entorno.
