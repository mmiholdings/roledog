
# 🧠 GENIE Audit Dashboard – AWS Amplify Deployment

This guide helps you host GENIE's Streamlit audit dashboard on AWS Amplify as a static site.

## Step-by-Step:

1. Run your Streamlit app locally and export to HTML:
```bash
streamlit run streamlit_audit_dashboard.py
```

2. Install static exporter:
```bash
pip install streamlit-to-html
```

3. Export to HTML:
```bash
streamlit-to-html streamlit_audit_dashboard.py --output audit_dashboard.html
```

4. Push `audit_dashboard.html` to GitHub in a new repo (e.g. `genie-amplify`)

5. Go to [https://console.aws.amazon.com/amplify](https://console.aws.amazon.com/amplify)

6. Click **New App → Host Web App → Connect GitHub → Select repo**

7. Select `main` branch and `build settings` = None

8. Hit deploy. Site will be live at: `https://<your-app>.amplifyapp.com`
