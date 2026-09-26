"""The agent loop.

Takes a user goal, lets the LLM decide which tools to call, runs them,
feeds the results back, and repeats until the LLM gives a final answer.
"""

import json

from agent.llm import chat_with_tools
from agent.tools.registry import TOOL_DEFINITIONS, TOOL_FUNCTIONS

MAX_STEPS = 8  # safety: never loop forever


def run_agent(goal: str, verbose: bool = True) -> str:
    """Run the agent loop for a single goal. Returns the final text answer."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful PC assistant running on Windows. "
                "You can list files and read files inside the user's home folder. "
                "Use tools when you need real information. "
                "When you have the answer, reply in plain text without calling tools."
            ),
        },
        {"role": "user", "content": goal},
    ]

    for step in range(1, MAX_STEPS + 1):
        if verbose:
            print(f"\n--- step {step} ---")

        msg = chat_with_tools(messages, TOOL_DEFINITIONS)
        messages.append(msg)

        tool_calls = msg.get("tool_calls") or []

        if not tool_calls:
            # No tools requested — final answer.
            return msg.get("content", "(no content)")

        # Run each requested tool.
        for call in tool_calls:
            name = call["function"]["name"]
            raw_args = call["function"].get("arguments") or {}

            # Ollama sometimes returns args as a JSON string; normalise it.
            if isinstance(raw_args, str):
                try:
                    args = json.loads(raw_args)
                except json.JSONDecodeError:
                    args = {}
            else:
                args = raw_args

            if verbose:
                print(f"[tool] {name}({args})")

            func = TOOL_FUNCTIONS.get(name)
            if func is None:
                result = f"Error: unknown tool '{name}'"
            else:
                try:
                    result = func(**args)
                except TypeError as e:
                    result = f"Error: bad arguments for {name}: {e}"

            if verbose:
                preview = str(result).splitlines()[0][:80] if result else ""
                print(f"       → {preview}")

            messages.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "content": str(result),
                }
            )

    return f"(stopped after {MAX_STEPS} steps without a final answer)"