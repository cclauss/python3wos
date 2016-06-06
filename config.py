import os

HTML_CACHE_KEY = 'WOShtml'
SERVER_SOFTWARE = 'SERVER_SOFTWARE'
server_software_str = os.getenv(SERVER_SOFTWARE, '')
LIVE = server_software_str.startswith('Google')      # remote google apps
DEV = server_software_str.startswith('Development')  # local dev server
GAE = LIVE or DEV
