from src.setup.migration import migrate
from src.setup.seed import seed_heroes, seed_patch, seed_changelog
from src.setup.teardown import teardown_db
from src.setup.create import create_database
from src.query import comment_to_query, get_ids, get_changelog
from src.db import get_db
from scripts.build import build
from scripts.reset import reset

class Testing():
    def __init__(self):
        self.db = None

    def initialize_db(self):
        self.db = get_db()

    def get_db(self):
        if self.db == None:
            self.initialize_db()
        return self.db

    def run(self):
        while 1:
            CHOICE = raw_input("What function?")
            QUERY_CHOICE = ""
            if CHOICE == "migrate":
                migrate(self.get_db())
                continue
            if CHOICE == "heroes":
                seed_heroes(self.get_db())
                continue
            if CHOICE == "patch":
                seed_patch(self.get_db())
                continue
            if CHOICE == "changelog":
                seed_changelog(self.get_db())
                continue
            if CHOICE == "query":
                QUERY_CHOICE = raw_input("Query? ")
                query = comment_to_query(QUERY_CHOICE)
                ids = get_ids(self.get_db(), query[0], query[1])
                print get_changelog(self.get_db(), ids[0], ids[1])
                continue
            if CHOICE == "teardown":
                teardown_db()
                continue
            if CHOICE == "create":
                create_database()
                continue
            if CHOICE == "build":
                build()
                continue
            if CHOICE == "reset":
                reset()
                continue
            if CHOICE == "end":
                break
            print "error"

if __name__ == '__main__':
    testing = Testing()
    testing.run()

