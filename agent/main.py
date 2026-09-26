"""PC Agent — Phase 2 test harness.

Proves the LLM wrapper and file tools work before we wire them together.
"""

from agent.llm import ask
from agent.tools.files import list_files, read_file


def main():
    print("=" * 50)
    print("Phase 2 test harness")
    print("=" * 50)

    # --- Test 1: LLM wrapper ---
    print("\n[1] Testing LLM wrapper...")
    reply = ask("Reply with exactly: LLM OK")
    print(f"    Model said: {reply.strip()}")

    # --- Test 2: list_files ---
    print("\n[2] Testing list_files('.'):")
    print(list_files("."))

    # --- Test 3: list_files on Downloads ---
    print("\n[3] Testing list_files('Downloads'):")
    print(list_files("Downloads"))

    # --- Test 4: sandbox escape attempt ---
    print("\n[4] Testing sandbox escape (should FAIL safely):")
    print(read_file(r"C:\Windows\System32\drivers\etc\hosts"))

    print("\n" + "=" * 50)
    print("Phase 2 test complete.")
    print("=" * 50)


if __name__ == "__main__":
    main()