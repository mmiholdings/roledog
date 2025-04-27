import redis
import openai
import json
from datetime import datetime

r = redis.Redis(host='localhost', port=6379)
samples = r.lrange("mo_buffer", 0, 10)
transitions = [json.loads(t.decode()) for t in samples]

prompt = f"""
Analyze this MARL replay buffer. Summarize:
- Agent behavior trends
- Reward anomalies
- Strategy improvements

{json.dumps(transitions, indent=2)}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

summary_file = f"agent_eval_summary_{datetime.utcnow().date()}.md"
with open(summary_file, "w") as f:
    f.write(response["choices"][0]["message"]["content"])