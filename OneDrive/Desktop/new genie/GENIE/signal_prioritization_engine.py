
def get_trusted_signal(signals):
    # signals = [{'source': 'Claude', 'score': 0.7}, {'source': 'Jurassic', 'score': 0.9}]
    trust_weights = {
        'Claude': 0.65,    # from signal_reputation table
        'Jurassic': 0.80,
        'Reggie': 0.72
    }
    scored = [(s['source'], s['score'] * trust_weights.get(s['source'], 0.5)) for s in signals]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0]  # return highest weighted signal
