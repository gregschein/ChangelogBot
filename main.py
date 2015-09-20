import praw
import ConfigParser
import OAuth2Util
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
REDIRECT_URI = config.get("Reddit", "redirect_uri")

r=praw.Reddit(USERAGENT)
r.login(USERNAME, PASSWORD)
# r.set_oauth_app_info(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
o = OAuth2Util.OAuth2Util(r)
o.refresh()
# subreddit = r.get_subreddit('dota2')

DONE = []
db = get_db()

def comment_is_valid(comment):

    comment = comment.replace("Changelog! ", "")
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
    with open("config/data/comments_done.cfg", "w") as f:
        for d in done:
            if d:
                f.write(d + "\n")

def main_loop():

    while True:
        done = read_config_done()
        new_done = []
        
        try:
            for comment in r.get_comments("dota2", limit=None):
                if "dota" in comment.body and comment.id not in done:
                    # match = comment_is_valid(comment.body)
                    # query = comment_to_query(match)
                    # ids = get_ids(db, query[0], query[1])
                    # changelog = get_changelog(db, ids[0], ids[1])
                    # print changelog
                    print comment.body
                    new_done.append(comment.id)
            write_config_done(new_done)
            print "looped"
            time.sleep(30)

        except:
            print "looped except"
            time.sleep(30)

if __name__ == "__main__":
    main_loop()