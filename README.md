
# Multi-Agent Enterprise Automation Platform

## Features
- Planner Agent
- Code Agent
- Documentation Agent
- Memory Store
- Groq LLM Integration
- FastAPI Backend

## Setup

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=your_key_here
```

## Run

```bash
uvicorn app.main:app --reload
```
