
# GENIE RenderOps Trigger Suite

## Components

- `render_weekly_summarizer.py`: Runs every week to summarize Render logs using Claude
- `slack_trigger_server.py`: Flask server to receive `/genie run <module>` Slack commands
- `render.yaml`: Multi-service Render deployment config
- `Procfile`: Used by Slack trigger microservice

## Slack Command Format

```
/genie run agent_memory_tracker
/genie run weight_config_builder
```

## GitHub Actions

Push this repo to GitHub. Render will auto-deploy using `render.yaml`.

