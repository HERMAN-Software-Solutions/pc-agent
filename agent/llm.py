"""LLM wrapper around Ollama.

Phase 2: simple chat + a test function.
Phase 3 will add tool-calling support on top of this.
"""

import ollama

MODEL = "qwen2.5:3b"


def chat(messages: list[dict]) -> str:
    """Send a list of chat messages to the model and return the reply text.

    messages is a list like:
        [{"role": "user", "content": "hello"}]
    """
    response = ollama.chat(model=MODEL, messages=messages)
    return response["message"]["content"]


def ask(prompt: str) -> str:
    """One-shot helper: send a single prompt, get a reply."""
    return chat([{"role": "user", "content": prompt}])