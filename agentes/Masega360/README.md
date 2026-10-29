# Mi agente

**Nombre:** Contador de palabras

**Autor:** [@Masega360](https://github.com/Masega360)

**Problema que resuelve:** Saber cuántas palabras tiene un texto, por ejemplo para no pasarte del límite de una consigna. También lee páginas web para resumirlas.

**Tools custom:**

- `contar_palabras(texto)`: devuelve la cantidad de palabras de un texto.

**Guardrail (hook):** `solo_sitios_permitidos` corre antes de cada tool y cancela cualquier `fetch` a un sitio que no esté en `SITIOS_PERMITIDOS`. Así el agente no lee cualquier página que le pasen.

**MCP y skills (suman puntos):**

- MCP: [`mcp-server-fetch`](https://pypi.org/project/mcp-server-fetch/), que le da la tool `fetch` para leer páginas web. Corre local con el mismo Python del venv.
- Skill: [`chequear-limite`](skills/chequear-limite/SKILL.md), que le enseña cómo responder si un texto entra en un límite de palabras.

**Cómo correrlo:**

```bash
pip install -r agentes/Masega360/requirements.txt
python agentes/Masega360/agent.py
```

Te pide pedidos por consola. Probá con:

- `¿La frase "hoy aprendí a crear agentes con Strands" entra en un límite de 5 palabras?` (tool + skill)
- `¿De qué trata https://strandsagents.com?` (MCP)
- `Leé https://example.com y resumila` (el guardrail la bloquea)
