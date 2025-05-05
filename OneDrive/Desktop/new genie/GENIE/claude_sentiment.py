import json
import boto3
import re

def lambda_handler(event, context):
    prompt = event.get("prompt", "")

    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    body = json.dumps({
        "prompt": f"\n\nHuman: Analyze this market update and return a sentiment score between -1 (bearish) and +1 (bullish), and a 1-sentence rationale.\nText: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 100,
        "temperature": 0.3
    })

    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=body
    )

    result = json.loads(response["body"].read())
    raw = result["completion"].strip()

    match = re.search(r'(-?\d+(?:\.\d+)?)', raw)
    score = float(match.group(1)) if match else 0.0

    return {
        "statusCode": 200,
        "body": json.dumps({
            "score": score,
            "rationale": raw
        })
    }
