
resource "aws_secretsmanager_secret" "genie_secrets" {
  name = "genie-secret"
  description = "Secrets for GENIE ML + Claude + Notion"
}

resource "aws_secretsmanager_secret_version" "genie_secrets_version" {
  secret_id     = aws_secretsmanager_secret.genie_secrets.id
  secret_string = jsonencode({
    CLAUDE_KEY = "xxx",
    NOTION_KEY = "xxx",
    PREDICTNOW_KEY = "xxx"
  })
}
