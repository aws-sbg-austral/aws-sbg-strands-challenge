# Strands Challenge 🧵

Challenge del **AWS Student Builder Group – Universidad Austral**.

Ya viste cómo funciona [Strands Agents](https://strandsagents.com): cómo crear un agente, invocarlo y darle tools. Ahora te toca a vos.

## La consigna

Creá un agente que **resuelva un problema real de tu día a día**.

Requisitos:

1. Hacé un **fork** de este repo y trabajá en tu fork.
2. Tu agente tiene que estar hecho **sí o sí con Strands Agents**. No vale otro framework (LangChain, CrewAI, etc.).
3. Tiene que tener **al menos una tool custom** definida por vos con `@tool`.
4. Entregalo abriendo un **Pull Request** a este repo (ver [Cómo entregar](#cómo-entregar)).

Ideas para arrancar: dividir gastos con amigos, armar la lista del súper, organizar tu semana de parciales, recomendarte qué cocinar con lo que tenés en la heladera, avisarte qué bondi te conviene... lo que te sirva a vos.

## Cómo arrancar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r agentes/Masega360/requirements.txt
python agentes/Masega360/agent.py
```

[`agentes/Masega360/`](agentes/Masega360/) es un ejemplo mínimo con una tool (`contar_palabras`) y el formato de entrega.

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

## Cómo entregar

1. En tu fork, duplicá la carpeta [`agentes/tu_nombre/`](agentes/tu_nombre/) con el nombre de tu usuario de GitHub (no la renombres: la plantilla tiene que quedar) y poné ahí todo lo tuyo:
   ```
   agentes/
   └── tu-usuario/
       ├── agent.py
       ├── README.md
       └── requirements.txt   # strands-agents[ollama] + cualquier librería extra que uses
   ```
   No toques archivos fuera de tu carpeta, así no hay conflictos con los demás.
2. Completá el `README.md` de tu carpeta (tenés uno de ejemplo en [`agentes/Masega360/`](agentes/Masega360/)):
   - **Nombre** del agente
   - **Problema** que resuelve
   - **Tools custom** que definiste y qué hace cada una
   - **Cómo correrlo**
3. Abrí un **Pull Request** desde tu fork a `main` de este repo, con el título `[Challenge] <nombre de tu agente>`.

> ⚠️ Nunca subas credenciales (keys de AWS, tokens, `.env`). Usá variables de entorno.
