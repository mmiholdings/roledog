
import cohere
co = cohere.Client('YOUR_API_KEY')

patterns = ["VWAP bounce breakout", "Gamma squeeze", "Liquidity sweep reversal"]
query = "High-volume trap above overnight high"

response = co.rerank(model='rerank-english-v2.0', query=query, documents=patterns)
for doc in response.results:
    print(f"Pattern: {doc.document}, Score: {doc.relevance_score}")
