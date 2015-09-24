import praw
from prawoauth2 import PrawOAuth2Server

import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config/botconfig.cfg")

USERNAME = config.get("Reddit", "username")
PASSWORD = config.get("Reddit", "password")
USERAGENT = config.get("Reddit", "useragent")
CLIENT_ID = config.get("Reddit", "client_id")
CLIENT_SECRET = config.get("Reddit", "client_secret")
SCOPES = config.get("Reddit", "scopes").split(", ")
r = praw.Reddit(user_agent = USERAGENT)
oauthserver = PrawOAuth2Server(r, app_key=CLIENT_ID,
                               app_secret=CLIENT_SECRET, state=USERAGENT,
                               scopes=SCOPES)
oauthserver.start()
tokens = oauthserver.get_access_codes()
print tokens