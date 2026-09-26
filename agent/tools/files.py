"""File tools for the PC Agent.

All operations are sandboxed to SANDBOX_ROOT.
Any attempt to escape (via .. or absolute paths outside) is blocked.
"""

import os
from pathlib import Path

# The only place the agent can touch. Change here to widen later.
SANDBOX_ROOT = Path(r"C:\Users\jaing").resolve()

# Max characters returned from a single read (keeps the LLM prompt sane).
MAX_READ_CHARS = 4000


def _safe_path(user_path: str) -> Path:
    """Resolve user_path inside SANDBOX_ROOT, or raise ValueError.

    Accepts:
      - relative paths ("Downloads", "notes.txt")
      - absolute paths inside the sandbox
    Rejects:
      - anything that resolves outside SANDBOX_ROOT
    """
    if os.path.isabs(user_path):
        candidate = Path(user_path).resolve()
    else:
        candidate = (SANDBOX_ROOT / user_path).resolve()

    # .resolve() collapses "..", so this catches escapes cleanly.
    if SANDBOX_ROOT not in candidate.parents and candidate != SANDBOX_ROOT:
        raise ValueError(f"Path escapes sandbox: {user_path}")

    return candidate


def list_files(directory: str = ".") -> str:
    """List entries in a directory inside the sandbox.

    Returns a newline-separated listing, or an error string.
    """
    try:
        target = _safe_path(directory)
        if not target.exists():
            return f"Error: not found: {directory}"
        if not target.is_dir():
            return f"Error: not a directory: {directory}"

        entries = sorted(target.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        lines = []
        for entry in entries[:100]:  # cap the listing
            marker = "[dir] " if entry.is_dir() else "[file]"
            lines.append(f"{marker} {entry.name}")

        if not lines:
            return f"(empty directory: {directory})"
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"


def read_file(path: str) -> str:
    """Read a text file inside the sandbox.

    Returns up to MAX_READ_CHARS characters, or an error string.
    """
    try:
        target = _safe_path(path)
        if not target.exists():
            return f"Error: not found: {path}"
        if not target.is_file():
            return f"Error: not a file: {path}"

        text = target.read_text(encoding="utf-8", errors="replace")
        if len(text) > MAX_READ_CHARS:
            return text[:MAX_READ_CHARS] + f"\n\n... [truncated, {len(text)} chars total]"
        return text
    except Exception as e:
        return f"Error: {e}"