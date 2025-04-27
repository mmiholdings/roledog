
#!/bin/bash
echo "🚀 Deploying GENIE Command Suite to Render/ECS..."
git add .
git commit -m "📦 Push updated GENIE execution modules"
git push origin main
echo "✅ Code pushed. Render/GitHub Actions will auto-deploy if configured."
