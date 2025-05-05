<#
    Run once per environment:
    -------------------------
      pwsh -ExecutionPolicy Bypass ./scripts/set_secrets.ps1 -Fly -Netlify
#>
param(
  [switch]$Fly,
  [switch]$Netlify
)
if ($Fly) {
  fly secrets set POSTGRES_URL=$env:POSTGRES_URL `
                  KC_BASE=$env:KC_BASE `
                  MINIO_ENDPOINT=$env:MINIO_ENDPOINT
}
if ($Netlify) {
  netlify env:set NEXT_PUBLIC_API_URL $env:NEXT_PUBLIC_API_URL
}
