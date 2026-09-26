"""PC Agent — interactive CLI.

Phase 3: the agent loop is live. Ask it things and watch it use tools.
"""

from agent.loop import run_agent


def main():
    print("=" * 50)
    print("PC Agent (Phase 3) — type 'quit' to exit")
    print("=" * 50)

    while True:
        try:
            goal = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not goal:
            continue
        if goal.lower() in {"quit", "exit", "q"}:
            print("Bye.")
            break

        answer = run_agent(goal, verbose=True)
        print(f"\nAgent: {answer}")


if __name__ == "__main__":
    main()