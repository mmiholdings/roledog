# RoleDogs 🐕‍🦺🎬
US‑based, open‑source audition & self‑taping platform.

## 📑 Index
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Quick Start (local)](#quick-start-local)
4. [Full Setup & Deployment](#full-setup--deployment)
   1. [Prerequisites](#prerequisites)
   2. [Environment (.env)](#environment-env)
   3. [Local Dev Workflow](#local-dev-workflow)
   4. [Production Deploy](#production-deploy)
      * [Fly.io (services)](#flyio-services)
      * [Netlify (front‑end)](#netlify-front-end)
   5. [Secrets Matrix](#secrets-matrix)
5. [Roadmap](#roadmap)
6. [Extended Docs](#extended-docs)

---

## Overview
| Layer | Tech |
|-------|------|
| **UI** | Next 14 (App Router) · Tailwind 3 |
| **Edge/API Functions** | Netlify Functions |
| **Core API** | Node Express + Keycloak 24 |
| **AI Worker** | GPT‑4‑All · DeepSpeech (Bull queue) |
| **Data** | Postgres 15 · Redis 7 · MeiliSearch 1.8 · MinIO S3 |
| **Video** | Self‑hosted Jitsi |
| **Cloud** | Netlify (frontend) · Fly.io (services) |

---

## Architecture
```mermaid
graph TD
  A[Next JS 14] -->|JWT| E(Keycloak 24)
  A -->|REST| B(API – Express)
  B --> C(Postgres):::db
  B --> D(Redis):::cache
  B --> F(MinIO):::storage
  B --> G(MeiliSearch):::search
  B --> H(Worker AI):::ai
  H --> D
  subgraph Video
    I[Jitsi Videobridge] -.-> J[Jicofo]
  end
