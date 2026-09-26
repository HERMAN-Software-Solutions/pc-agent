"""LLM wrapper around Ollama.

Phase 2: simple chat + a test function.
Phase 3: adds tool-calling support.
"""

import ollama

MODEL = "qwen2.5:3b"


def chat(messages: list[dict]) -> str:
    """Send a list of chat messages to the model and return the reply text."""
    response = ollama.chat(model=MODEL, messages=messages)
    return response["message"]["content"]


def ask(prompt: str) -> str:
    """One-shot helper: send a single prompt, get a reply."""
    return chat([{"role": "user", "content": prompt}])


def chat_with_tools(messages: list[dict], tools: list[dict]) -> dict:
    """Send messages + tool definitions, return the raw assistant message.

    The returned dict is the 'message' field from Ollama. It may contain:
      - 'content': normal text reply
      - 'tool_calls': a list of tools the model wants to run
    """
    response = ollama.chat(model=MODEL, messages=messages, tools=tools)
    return response["message"]