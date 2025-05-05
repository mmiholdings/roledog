
# ✅ GENIE 3.0 Full Deployment Guide (for Dave, Tee, Aaron)

## 🧱 Prerequisites:
- GitHub account with access to GENIE repo
- AWS CLI installed
- IAM user with ECR, ECS, SecretsManager, EC2, CloudWatch access
- SSH key to EC2
- Slack admin access (to install GENIE app)

---

## 🧪 LOCAL TEST

```bash
make test     # Run local tests
make build    # Build GENIE Docker image
make run      # Run locally
make push     # Push image to ECR
```

---

## 🚀 EC2 + ECR Deployment
1. SSH into EC2
2. Run: `./bootstrap_institution.sh`
3. Confirm:
   - Docker is running
   - GENIE repo cloned
   - GENIE service is running in `docker ps`

---

## 🌐 ECS Streamlit Deployment (Terraform)
1. Update `terraform_streamlit_service.tf` with:
   - Your subnet ID
   - Your security group
2. Run:
```bash
terraform init
terraform apply
```
3. Open the assigned ECS public IP: `http://<ip>:8501`

---

## 🔘 Slack Button Setup
1. Go to https://api.slack.com/apps → Create App
2. Add interactive message blocks (use provided JSON)
3. Install to workspace
4. `/genie status` → Shows dashboard link

---

## ✅ Claude/GPT Weekly Loop

- Claude summarizes logs every Sunday
- Output auto-posted to Notion DB
- Dashboard updates reflect:
  - Completed audits
  - Failed logs
  - GPT insights

---

## 📋 Apps + Scripts + Tools Needed
| Tool | Purpose |
|------|---------|
| GitHub Actions | Auto-push to EC2/ECR |
| Docker | Container for GENIE engine |
| Terraform | Infra provisioning (ECS, secrets) |
| n8n | Claude integration, scheduling |
| AWS Secrets Manager | API keys (Claude, Notion, PredictNow) |
| CloudWatch | GENIE log archive |
| Streamlit | Audit dashboard |
| Slack | Deployment trigger & dashboard viewer |
| Notion | Audit log storage |

---

This guide brings GENIE 3.0 to institutional execution level, no DevOps needed.
