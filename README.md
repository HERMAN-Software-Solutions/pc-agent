# PC Agent

A local AI agent for Windows, built phase by phase.

## Status
- [x] Phase 0 — Setup (Git, Python, Ollama)
- [ ] Phase 1 — Skeleton
- [ ] Phase 2 — First tool
- [ ] Phase 3 — Agent loop
- [ ] Phase 4 — Safety
- [ ] Phase 5 — Memory
- [ ] Phase 6 — Extend

## Stack
- Windows
- Python 3.14
- Ollama (`qwen2.5:3b`)
- Git

## Setup
1. Install Ollama — https://ollama.com/download/windows
2. Pull the model:
ollama pull qwen2.5:3b

text
3. Install Python deps:
py -m pip install -r requirements.txt

text
4. Run:
py -m agent.main

text

## Roadmap
See [docs/roadmap.md](docs/roadmap.md).