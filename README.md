# Folder Therapy

> Your messy file system gets a family-therapy session and rename prescriptions.

An AI tool scans a folder tree and treats it like a dysfunctional household, identifying hoarded files, orphaned downloads, and name conflicts. It gives each folder a diagnosis and suggests moves, renames, and deletion rituals.

## Features
- Scan a directory tree and build a family tree of files and folders
- Use an LLM to diagnose clutter, naming conflicts, and abandoned projects
- Generate safe rename and move suggestions with confidence scores
- Export a therapy report and a review queue for applying changes

## Stack
- Python
- FastAPI
- OpenAI

## Getting started
```
Install dependencies with `pip install -r requirements.txt`, set `OPENAI_API_KEY`, then run `uvicorn app.main:app --reload` and open `http://localhost:8000`.
```

---
*Farmed 🚜 by [Appshaker](https://github.com/buberlo) — shaken into existence.*
