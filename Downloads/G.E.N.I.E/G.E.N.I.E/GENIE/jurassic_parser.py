import json
import boto3

def lambda_handler(event, context):
    filing_text = event.get("filing", "")

    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    prompt = f"""Extract the following structured fields from this SEC filing or dark pool log:
- Ticker
- Event Type (e.g., Insider Buy, Earnings Miss, Large Dark Pool Print)
- Directional Bias (Bullish, Bearish, Neutral)
- Summary
Text:
{filing_text}
Respond as JSON:
"""

    body = json.dumps({
        "prompt": prompt,
        "maxTokens": 200,
        "temperature": 0.2,
        "stopSequences": ["\n\n"]
    })

    response = client.invoke_model(
        modelId="ai21.j2-ultra-v1",
        contentType="application/json",
        accept="application/json",
        body=body
    )

    parsed = json.loads(response["body"].read())
    structured = parsed.get("completion", "{}")

    return {
        "statusCode": 200,
        "body": structured
    }
