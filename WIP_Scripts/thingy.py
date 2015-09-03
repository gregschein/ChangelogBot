from src.setup.migration import migrate
from src.setup.seed import seed_heroes, seed_patch
from src.setup.teardown import teardown_db
from src.setup.create import create_database
from src.query import comment_to_query
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
            if CHOICE == "query":
                QUERY_CHOICE = raw_input("Query? ")
                comment_to_query(QUERY_CHOICE)
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

if __name__ == '__main__':
    testing = Testing()
    testing.run()

