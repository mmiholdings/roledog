
resource "grafana_dashboard" "genie_agents" {
  config_json = file("${path.module}/agent_leaderboard_dashboard.json")
  folder      = "GENIE"
  overwrite   = true
  depends_on  = [grafana_datasource.postgres]
}

resource "grafana_datasource" "postgres" {
  name = "PostgreSQL GENIE"
  type = "postgres"
  url  = "genie-postgres:5432"
  database_name = "geniedb"
  user = "genie"
  secure_json_data = {
    password = "geniepass"
  }
}
