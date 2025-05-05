#!/usr/bin/env bash
cp infra/.env.example infra/.env 2>/dev/null || true
cd frontend && yarn && cd ..
echo "Local dev ready: docker compose -f infra/docker-compose.dev.yml up -d && yarn dev"
