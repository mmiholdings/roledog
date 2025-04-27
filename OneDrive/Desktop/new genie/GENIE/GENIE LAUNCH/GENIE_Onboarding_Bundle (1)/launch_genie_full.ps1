Write-Host "🧠 Launching GENIE Full Deployment..."

# Activate virtual environment if it exists
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    Write-Host "✅ Activating virtual environment..."
    .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠️ No virtual environment found — continuing anyway"
}

# Start AI Agent Scripts
Write-Host "🚀 Starting AI Agents..."
Start-Process powershell -ArgumentList 'python train_mo.py' -NoNewWindow
Start-Process powershell -ArgumentList 'python train_marl.py' -NoNewWindow
Start-Process powershell -ArgumentList 'python signal_sender.py' -NoNewWindow

# Launch Streamlit Dashboard
Write-Host "📺 Launching GENIE Dashboard..."
Start-Process powershell -ArgumentList 'streamlit run streamlit_terminal_dashboard.py' -NoNewWindow

# Optional Docker Compose (if installed)
if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    Write-Host "🐳 Launching Docker Services..."
    Start-Process powershell -ArgumentList 'docker-compose up --build -d' -NoNewWindow
} else {
    Write-Host "⚠️ Docker not found — skipping containerized launch"
}

Write-Host "✅ GENIE Fully Deployed. Check your browser at http://localhost:8501"