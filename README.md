# PocketSmart AI

Complete FastAPI + Jinja2 implementation of the supplied PocketSmart AI project documentation.

## What is included
- Home Interior Planner
- Party Budget Planner
- Jewelry Planner with optional outfit-image input
- Gemini multimodal integration
- JWT authentication
- SQLite database and recommendation history
- Responsive HTML/CSS/JavaScript frontend
- Mock platform catalog/search links for Amazon, Flipkart, IKEA, Swiggy, Zomato and OYO
- Deterministic fallback recommendations when Gemini is unavailable
- Automated API tests

## Source-document implementation decision
The supplied document uses both Flask and FastAPI wording, but its later milestones explicitly require FastAPI, `main.py`, Uvicorn and FastAPI routes. This implementation uses FastAPI consistently.

The document names Gemini 1.5 Flash Pro. That is not a suitable default for a new 2026 implementation, so the model is configurable and defaults to `gemini-3.8-flash`. Change `GEMINI_MODEL` in `.env` if needed.

## Run in VS Code — Windows
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

API docs: http://127.0.0.1:8000/docs

## macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Gemini
Put your API key in `.env`:
`GEMINI_API_KEY=your_key_here`

Without a key, all planners still work using the built-in fallback catalog.

## Test
```bash
pytest -q
```
