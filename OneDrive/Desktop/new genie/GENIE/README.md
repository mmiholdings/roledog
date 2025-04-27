# GENIE 3.0 Docker Deploy Kit (For Beginners)

## Step-by-Step Instructions

### 1. Install Docker
On Ubuntu:
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
```

### 2. Clone the GENIE Repo
```bash
git clone https://github.com/your-org/genie-live.git
cd genie-live
```

### 3. Build and Run Containers
```bash
docker-compose up -d
```

### 4. Confirm Services
```bash
docker ps
```

### 5. Access Interfaces
- Streamlit: http://localhost:8501
- PostgreSQL: localhost:5432
- n8n: http://localhost:5678

### 6. Run Sample Training
```bash
python3 train_agent_harness.py
```