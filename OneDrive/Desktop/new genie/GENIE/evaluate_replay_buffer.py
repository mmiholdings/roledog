import redis
import openai
import json

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

with open("claude_feedback_summary.md", "w") as f:
    f.write(response["choices"][0]["message"]["content"])

print("✅ Saved Claude feedback summary.")