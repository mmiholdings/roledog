import redis
import json
import random

r = redis.Redis(host='localhost', port=6379)

for _ in range(100):
    state = [random.random() for _ in range(5)]
    action = random.randint(0, 2)
    reward = random.uniform(-1, 1)
    next_state = [s + random.uniform(-0.01, 0.01) for s in state]
    done = random.choice([True, False])
    transition = {"s": state, "a": action, "r": reward, "s'": next_state, "done": done}
    r.lpush("mo_buffer", json.dumps(transition))

print("✅ Sample transitions written to Redis buffer")