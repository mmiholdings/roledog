
---

## 2  docs/ARCHITECTURE.md

```markdown
# RoleDogs — System Architecture

```mermaid
graph TD
  A[Next JS 14\n(Netlify)] -->|JWT| E(Keycloak 24)
  A -->|REST| B(API – Express)
  B --> C(Postgres 15):::db
  B --> D(Redis 7):::cache
  B --> F(MinIO S3):::storage
  B --> G(MeiliSearch 1.8):::search
  B --> H(Worker AI):::ai
  H --> D
  subgraph Video
    I[Jitsi Videobridge] -.-> J[Jicofo]
  end
  classDef db fill:#ffefcf,stroke:#cfa
  classDef cache fill:#ffd,stroke:#f70
  classDef storage fill:#def,stroke:#09f
  classDef search fill:#dfd,stroke:#090
  classDef ai fill:#fed,stroke:#f80
