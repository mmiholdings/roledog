
import time
import random

def simulate_ticks(symbol="ES", interval=1):
    price = 4500.0
    while True:
        delta = random.uniform(-1.5, 1.5)
        price += delta
        print(f"TICK {symbol}: {price:.2f}")
        time.sleep(interval)

if __name__ == "__main__":
    simulate_ticks()
