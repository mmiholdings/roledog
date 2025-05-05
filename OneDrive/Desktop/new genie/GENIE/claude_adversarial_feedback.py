
# Claude → MARL Feedback Loop: Did the agent ignore sentiment bias?

import requests

def compare_trade_vs_claude(entry_text, trade_result):
    prompt = f"""
You are GENIE's oversight AI. A trade was executed under the following logic:

ENTRY:
{entry_text}

RESULT:
{trade_result}

Was the trade consistent with Claude's sentiment? If not, advise whether this was a good exception or a mistake.
"""

    response = requests.post("https://your-api.com/claude-feedback", json={"prompt": prompt})
    print("🧠 Claude Feedback:", response.text)
