#!/bin/bash
# GENIE AIOCC EC2 Bootstrap Script

# Update system
sudo apt update -y && sudo apt upgrade -y

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Streamlit and required packages
pip3 install streamlit pandas matplotlib requests

# Install Docker
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Pull PostgreSQL and Grafana containers
sudo docker network create genie-net
sudo docker run -d --name genie-postgres --network genie-net -e POSTGRES_USER=genie -e POSTGRES_PASSWORD=geniepass -e POSTGRES_DB=geniedb -p 5432:5432 postgres
sudo docker run -d --name genie-grafana --network genie-net -p 3000:3000 grafana/grafana

# Enable ports for Streamlit and Grafana
sudo ufw allow 8501
sudo ufw allow 3000
