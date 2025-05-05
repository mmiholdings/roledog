# RoleDogs 🐕‍🦺🎬

US based, Open‑source audition & self‑taping platform .

| Layer                  | Tech                                               |
| ---------------------- | -------------------------------------------------- |
| **UI**                 | Next 14 (App Router) · Tailwind 3                  |
| **Edge/API Functions** | Netlify Functions                                  |
| **Core API**           | Node Express + Keycloak 24                         |
| **AI Worker**          | GPT‑4‑All · DeepSpeech (Bull queue)                |
| **Data**               | Postgres 15 · Redis 7 · MeiliSearch 1.8 · MinIO S3 |
| **Video**              | Self‑hosted Jitsi                                  |
| **Cloud**              | Netlify (frontend) · Fly.io (services)             |

Quick start:

```bash
docker compose -f infra/docker-compose.dev.yml up -d
cd frontend && yarn dev          # http://localhost:3000
```
