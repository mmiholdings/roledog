# GENIE Multi-Agent Trading System

Welcome to the GENIE AI stack — a reinforcement-learning powered multi-agent execution system inspired by BlackRock’s Aladdin.

## 🚀 Core Components
- Multi-agent signal generators (Mo, Ace, Reggie, etc.)
- Claude-based reward and strategy audit
- Streamlit dashboards (Terminal, Training, Audit)
- GitHub Actions / Docker / EC2 ready
- S3 cloud storage of models and buffers

## 📁 Folder Structure
- `/agents/` - AI trading agents
- `/buffer/` - Replay memory for training
- `/dashboard/` - Streamlit dashboards
- `/audit/` - Claude summary & Telegram alerts

## 🧠 Get Started
```bash
docker-compose up --build
```

## 📦 Requirements
See `requirements.txt` for full package list