import json
from datetime import datetime

def summarize_buffer(buffer_path="/buffer/mes_buffer.json"):
    with open(buffer_path) as f:
        buffer = json.load(f)

    avg_reward = sum(x[2] for x in buffer) / len(buffer)
    win_rate = sum(1 for x in buffer if x[2] > 0) / len(buffer)
    summary = f"""
🧠 CLAUDE SUMMARY - {datetime.utcnow().isoformat()}

- Transitions: {len(buffer)}
- Avg Reward: {round(avg_reward, 4)}
- Win Rate: {round(win_rate*100, 2)}%
- Suggest: Adjust reward shaping if win rate < 60% or avg reward < 0.5
📁 Source: {buffer_path}
    """
    print(summary)
    with open("audit/claude_summary.md", "w") as f:
        f.write(summary)

if __name__ == "__main__":
    summarize_buffer()