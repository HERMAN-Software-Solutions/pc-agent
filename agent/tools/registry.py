"""Tool registry.

Defines the tools the agent can call, in the format Ollama expects,
and maps each tool name to its Python function.
"""

from agent.tools.files import list_files, read_file


# --- Tool definitions (what the LLM sees) ---
TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": (
                "List files and folders inside a directory. "
                "Use '.' for the home folder. Paths are sandboxed to the user folder."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Relative path, e.g. 'Downloads' or '.'. Defaults to '.'.",
                    }
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read the text contents of a file inside the sandbox. "
                "Returns up to 4000 characters."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path to the file, e.g. 'notes.txt'.",
                    }
                },
                "required": ["path"],
            },
        },
    },
]


# --- Name → function map (what the loop actually calls) ---
TOOL_FUNCTIONS = {
    "list_files": list_files,
    "read_file": read_file,
}