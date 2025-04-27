
Write-Host "🔁 Launching Full GENIE AI Terminal with Agents + Docker..."

# Navigate to GENIE Core Directory
cd $PSScriptRoot

# Optional: Activate virtual environment if exists
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    .\venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual environment activated"
} else {
    Write-Host "⚠️  No virtual environment found — continuing anyway"
}

# Launch AI Agents
Start-Process powershell -ArgumentList 'python train_mo.py' -NoNewWindow
Start-Process powershell -ArgumentList 'python train_marl.py' -NoNewWindow
Start-Process powershell -ArgumentList 'python signal_sender.py' -NoNewWindow

# Launch Streamlit Dashboard
Start-Process powershell -ArgumentList 'streamlit run streamlit_terminal_dashboard.py' -NoNewWindow

# Start Docker Services
Start-Process powershell -ArgumentList 'docker-compose up --build -d' -NoNewWindow

Write-Host "🚀 GENIE is now launching... Check your browser at http://localhost:8501"
