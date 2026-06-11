# Multi-Agent-Research-System

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=ff8c32&height=120&section=header&text=ResearchMind&fontSize=40&fontColor=ffffff&fontAlignY=38" />

### *Not your average research tool.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-FF6B35?style=flat)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/status-active-50c878?style=flat)

</div>

---

## What is this?

A multi-agent system that does your research for you.

You give it a topic. It figures out the rest.

> *Details? You'll have to run it yourself.*

---

## How it works

```
input → [agent 1] → [agent 2] → [agent 3] → [agent 4] → output
```

Four agents. Each one knows its job. None of them need babysitting.

---

## Stack

- 🧠 **LLMs** via Groq
- 🔗 **LangChain + LangGraph** for agent orchestration
- 🌐 **Web search** — no paid APIs
- 🖥 **Streamlit** for the UI
- 🐍 **Python** all the way down

---

## Getting Started

```bash
git clone https://github.com/kashyapishika/ResearchMind
cd ResearchMind
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Add your key to `.env`:
```
GROQ_API_KEY=your_key_here
```
Get one free at [console.groq.com](https://console.groq.com)

Then:
```bash
python -m streamlit run app.py
```

---

## Requirements

- Python 3.10+
- A free Groq API key
- Curiosity

---

<div align="center">

*Built by [@kashyapishika](https://github.com/kashyapishika)*

<img src="https://capsule-render.vercel.app/api?type=waving&color=ff8c32&height=80&section=footer" />

</div>
