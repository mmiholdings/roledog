<#
  netlify_bootstrap.ps1 – creates Netlify site & env
#>
$siteName = "roledogs-$(Get-Random)"
$apiURL   = "https://roledogs-api.fly.dev"

Write-Host "🕸️  Creating Netlify site '$siteName'..."
$siteJSON = netlify sites:create --name $siteName --json | ConvertFrom-Json
$siteId   = $siteJSON.id
netlify env:set NEXT_PUBLIC_API_URL $apiURL --site $siteId | Out-Null

Write-Host "`n🔑  Netlify site created!"
Write-Host "   • Site ID         : $siteId"
Write-Host "   • Deploy URL      : $($siteJSON.ssl_url)"
Write-Host "   • Env NEXT_PUBLIC_API_URL -> $apiURL"
