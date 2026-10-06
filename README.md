# Strands Challenge 🧵

Challenge del **AWS Student Builder Group – Universidad Austral**.

Ya viste cómo funciona [Strands Agents](https://strandsagents.com): cómo crear un agente, invocarlo y darle tools. Ahora te toca a vos.

## La consigna

Creá un agente que **resuelva un problema real de tu día a día**.

Requisitos:

1. Hacé un **fork** de este repo y trabajá en tu fork.
2. Tu agente tiene que usar **Strands Agents**.
3. Tiene que tener **al menos una tool custom** definida por vos con `@tool`.
4. Reemplazá la sección [Mi agente](#mi-agente) de este README contando qué problema resuelve y cómo correrlo.

Ideas para arrancar: dividir gastos con amigos, armar la lista del súper, organizar tu semana de parciales, recomendarte qué cocinar con lo que tenés en la heladera, avisarte qué bondi te conviene... lo que te sirva a vos.

## Cómo arrancar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python agent.py
```

`agent.py` tiene un ejemplo mínimo con una tool (`contar_palabras`). Usalo de base y cambiale todo.

### Modelo

Por defecto Strands usa **Claude en Amazon Bedrock** (región `us-west-2`), así que necesitás credenciales de AWS configuradas (`aws configure` o variables de entorno) y acceso al modelo habilitado en Bedrock.

Si querés usar otro proveedor, mirá la sección *Model Providers* en la [doc de Strands](https://strandsagents.com).

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

Compartí el link a tu fork con el README completo.

---

## Mi agente

> Completá esta sección en tu fork.

**Nombre:**

**Problema que resuelve:**

**Tools custom:**

**Cómo correrlo:**
