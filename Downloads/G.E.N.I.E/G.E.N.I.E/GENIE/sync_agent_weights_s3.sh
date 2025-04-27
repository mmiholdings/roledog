#!/bin/bash
DATE=$(date +%F)
BUCKET="s3://genie-weights"
FILE="agent_weights.md"

if [ -f "$FILE" ]; then
  aws s3 cp $FILE $BUCKET/$DATE.md
  echo "✅ Synced $FILE to $BUCKET/$DATE.md"
else
  echo "⚠️ $FILE not found. Nothing to sync."
fi
