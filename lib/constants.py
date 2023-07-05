# REST API request constants
API_URL_SITES = 'https://central-service.commpay.aws-wealth-staging-au.iress.online/api/SiteRegistry/Sites?environment=stag&includeTenants=false&includeEmptySites=false'
API_ENDPOINT_HEALTHCHECK = '/commpay/Main/HealthCheck.aspx?key=84D987C4-9D2A-49F8-803F-183A79DB94AB'

# HTML elements that must be present to consider site to be healthy
HTML_GOOD_HEALTH_ELEMENTS = ['<title>CommPay Health Check</title>',
    '<td>SQL Server</td>', '<span id="lblDatabaseConnectionStatus" class="LabelStd">OK</span></td>']

# Health check status
HEALTHCHECK_FAILURE = 'Healthcheck API call failure'
HEALTHCHECK_GOOD = 'HEALTHY'
HEALTHCHECK_BAD = 'UNHEALTHY'