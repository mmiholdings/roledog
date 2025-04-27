#!/bin/bash
echo "🔄 Fetching Notion toggle to redeploy MARL agents..."

AGENT=$(curl -s -H "Authorization: Bearer $NOTION_TOKEN" https://api.notion.com/v1/pages/$PAGE_ID | jq -r '.properties.AgentName.title[0].text.content')
RETRAIN=$(curl -s -H "Authorization: Bearer $NOTION_TOKEN" https://api.notion.com/v1/pages/$PAGE_ID | jq -r '.properties.Retrain.checkbox')

if [ "$RETRAIN" = "true" ]; then
    echo "🚀 Redeploying agent: $AGENT"
    docker-compose restart $AGENT
else
    echo "⛔ Retrain not toggled."
fi