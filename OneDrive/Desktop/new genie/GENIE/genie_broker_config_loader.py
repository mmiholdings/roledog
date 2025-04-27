import json

def load_broker_configs(config_file="config.json"):
    with open(config_file, "r") as f:
        return json.load(f)["brokers"]