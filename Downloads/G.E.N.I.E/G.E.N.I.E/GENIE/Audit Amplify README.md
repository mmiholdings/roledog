
# ✅ GENIE Final Deployment ReadMe

## Components:

- `streamlit-to-html` exporter: converts Streamlit to static dashboard
- `webhook_server.py`: listens for Slack, Claude, or audit loop triggers
- `audit_static_archive.sh`: pushes to `gh-pages` branch for GitHub Pages site

## Slack Integration:

1. Configure webhook URL: `/audit-webhook`
2. Use with n8n or Claude audit triggers to POST summary + status

## Static Archive Usage:

Run:
```bash
bash audit_static_archive.sh
```

This publishes `audit_dashboard.html` to:
➡️ https://your-org.github.io/genie-audit
