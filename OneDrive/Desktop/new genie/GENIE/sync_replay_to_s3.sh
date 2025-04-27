#!/bin/bash
DATE=$(date +%F)
BUCKET="s3://genie-agent-memory"
REDIS_DUMP="/var/lib/docker/volumes/genie_redis_data/_data/dump.rdb"

if [ -f "$REDIS_DUMP" ]; then
  aws s3 cp "$REDIS_DUMP" "$BUCKET/$DATE.rdb"
  echo "✅ Synced $REDIS_DUMP to $BUCKET/$DATE.rdb"
else
  echo "❌ Redis dump.rdb not found."
fi