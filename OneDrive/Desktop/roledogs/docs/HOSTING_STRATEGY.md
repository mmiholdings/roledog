# Hosting Strategy

| Concern | Platform | Why |
|---------|----------|-----|
| Static + SSR | **Netlify** | Previews, atomic deploys, global CDN |
| Containers | **Fly.io** | App‑per‑service, autoscale, volumes |
| Secrets | GitHub Secrets · Fly Secrets | Single source for CI/CD |
| Domains | Cloudflare DNS | Easy TXT + A/AAAA management |

### CI/CD Pipeline

```text
push → GitHub Actions
 ├─ frontend-netlify.yml  → Netlify CLI deploy
 └─ backend-fly.yml (matrix api, worker, keycloak) → flyctl deploy
