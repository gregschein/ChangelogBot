from src.db import get_db
from src.setup.create import create_database
from src.setup.migration import migrate
from src.setup.seed import seed_heroes, seed_patch, seed_changelog

def build():
    """Creates database, migrates, and seeds"""

    create_database()
    database = get_db()
    migrate(database)
    seed_patch(database)
    seed_heroes(database)
    seed_changelog(database)
