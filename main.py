import praw
import ConfigParser
# import OAuth2Util
from prawoauth2 import PrawOAuth2Server, PrawOAuth2Mini
import re 
import time
from src.query import comment_to_query, get_ids, get_changelog
from src.db import get_db


config = ConfigParser.ConfigParser()
config.read("config/botconfig.cfg")
USERNAME = config.get("Reddit", "username")
PASSWORD = config.get("Reddit", "password")
USERAGENT = config.get("Reddit", "useragent")
CLIENT_ID = config.get("Reddit", "client_id")
CLIENT_SECRET = config.get("Reddit", "client_secret")
ACCESS_TOKEN = config.get("Reddit", "access_token")
REFRESH_TOKEN = config.get("Reddit", "refresh_token")
SCOPES = config.get("Reddit", "scopes").split(", ")


r=praw.Reddit(USERAGENT)
# r.login(USERNAME, PASSWORD)
# r.set_oauth_app_info(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
# o = OAuth2Util.OAuth2Util(r)
# o.refresh()


oauth_helper = PrawOAuth2Mini(
    r, 
    app_key=CLIENT_ID, 
    app_secret=CLIENT_SECRET,
    access_token=ACCESS_TOKEN,
    scopes=SCOPES,
    refresh_token=REFRESH_TOKEN
    )

DONE = []
db = get_db()

def comment_is_valid(comment):

    if re.match('[a-zA-Z\s]+ \d\.\d\d[a-z]?(\-\d\.\d\d[a-z]?)?', comment):
        return True
    else:
        return False

def read_config_done():
    done = []
    try:
        with open("config/data/comments_done.cfg", "r") as f:
            for line in f:
                if line.strip():
                    done.append(line.strip())
    except OSError:
        print("config/data/comments_done.cfg", "not found.")
    return done
    
def write_config_done(done):
    with open("config/data/comments_done.cfg", "a") as f:
        for d in done:
            if d:
                f.write(d + "\n")

def reply_to_comment(comment, changelog, hero_name):
    patch_template = "**{0}**\n\n"
    changes_template = "* {0}\n\n"
    reply = hero_name.title() + "\n____\n"
    for patch in changelog:
        reply += patch_template.format(patch[1])
        storage = patch[0].split(". ")
        for change in storage:
            reply += changes_template.format(change)
    comment.reply(reply)

def main_loop():

    while True:
        done = read_config_done()
        new_done = []
        try:
            oauth_helper.refresh()
            for comment in r.get_comments("test", limit=None):
                if "Changelog!" in comment.body and comment.id not in done:
                    comment_info = comment.body.replace("Changelog! ", "")
                    match = comment_is_valid(comment_info)
                    if not match:
                        continue
                    query = comment_to_query(comment_info)
                    hero_name = query[0][1][0]
                    ids = get_ids(db, query[0], query[1])
                    changelog = get_changelog(db, ids[0], ids[1])
                    reply_to_comment(comment, changelog, hero_name)
                    new_done.append(comment.id)
                    done.append(comment.id)
            write_config_done(new_done)
            print "before sleep"
            time.sleep(5)
            print "looped"
        except praw.errors.OAuthInvalidToken:
            print "fuck 2"
            oauth_helper.refresh()
            time.sleep(30)


if __name__ == "__main__":
    main_loop()