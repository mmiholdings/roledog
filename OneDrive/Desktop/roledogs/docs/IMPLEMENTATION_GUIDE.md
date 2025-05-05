
---

## 4  docs/IMPLEMENTATION_GUIDE.md

```markdown
# Implementation Guide

> MVP target: upload self‑tape → searchable dashboard in under 60 minutes.

---

## 1. Prerequisites

| Local | Cloud |
|-------|-------|
| Docker ≥ 24 | Netlify account |
| Node 20 + Yarn | Fly.io account |
| GitHub CLI | Postgres DB via Fly Postgres |

Clone & bootstrap:

```bash
git clone https://github.com/mmiholdings/roledog.git
cd roledog && ./scripts/post-clone.sh
