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

[`agentes/Masega360/`](agentes/Masega360/) es un ejemplo mínimo con una tool (`contar_palabras`) y el formato de entrega. Copiá esa carpeta con tu usuario y cambiale todo.

### Modelo

Por defecto Strands usa **Claude en Amazon Bedrock** (región `us-west-2`), así que necesitás credenciales de AWS configuradas (`aws configure` o variables de entorno) y acceso al modelo habilitado en Bedrock.

Si querés usar otro modelo (sigue siendo Strands, solo cambia el proveedor del LLM), mirá la sección *Model Providers* en la [doc de Strands](https://strandsagents.com).

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

1. En tu fork, creá la carpeta `agentes/<tu-usuario-de-github>/` y poné ahí todo lo tuyo:
   ```
   agentes/
   └── tu-usuario/
       ├── agent.py
       ├── README.md
       └── requirements.txt   # strands-agents + cualquier librería extra que uses
   ```
   No toques archivos fuera de tu carpeta, así no hay conflictos con los demás.
2. En tu `README.md` contá:
   - **Nombre** del agente
   - **Problema** que resuelve
   - **Tools custom** que definiste y qué hace cada una
   - **Cómo correrlo**
3. Abrí un **Pull Request** desde tu fork a `main` de este repo, con el título `[Challenge] <nombre de tu agente>`.

> ⚠️ Nunca subas credenciales (keys de AWS, tokens, `.env`). Usá variables de entorno.
