import redis
import json
import openai
from datetime import datetime

r = redis.Redis(host='localhost', port=6379)
samples = r.lrange("mo_buffer", 0, 100)
transitions = [json.loads(t.decode()) for t in samples]

prompt = f"""
You're Claude, reviewing MARL agent performance logs.
Summarize reward shaping issues, training imbalances, or policy gaps.

Sample transitions:
{json.dumps(transitions, indent=2)}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

with open("agent_training_summary.md", "w") as f:
    f.write(response["choices"][0]["message"]["content"])

print("✅ Claude feedback saved to agent_training_summary.md")