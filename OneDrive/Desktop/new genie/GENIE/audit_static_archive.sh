
#!/bin/bash
# Pushes weekly audit markdown or HTML summary to GitHub Pages branch

git checkout --orphan gh-pages
git rm -rf .
cp ./audit_dashboard.html index.html
git add index.html
git commit -m "🧠 Weekly Audit Update"
git push origin gh-pages --force
git checkout main
