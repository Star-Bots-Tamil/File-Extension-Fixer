import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # star bots client config
    API_ID    = os.environ.get("API_ID", "11973721")
    API_HASH  = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7713324413:AAFmzBFWAliE7cpUp_oq2qhX2UC-4INSGzM") 

    # other configs
    BOT_UPTIME  = time.time()
    ADMINS      = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1391556668 5162208212 5239847373').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
