#!/bin/bash
echo "🧠 Setting up GENIE Training Environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Environment ready."