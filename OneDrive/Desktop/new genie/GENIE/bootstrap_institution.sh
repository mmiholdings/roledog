#!/bin/bash

echo "🔧 Updating system..."
sudo apt update -y || sudo yum update -y

echo "📦 Installing core tools..."
sudo apt install -y git python3 python3-pip docker.io docker-compose unzip || sudo yum install -y git python3 python3-pip docker unzip

echo "🐳 Enabling Docker..."
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

echo "📂 Cloning GENIE repository..."
git clone https://github.com/YOUR-ORG/GENIE.git /opt/genie
cd /opt/genie

echo "⚙️ Setting up Docker Compose services..."
docker-compose -f docker-compose.yml up -d

echo "✅ GENIE stack deployed: Grafana, Prometheus, PostgreSQL, n8n"
