from src.db import get_db
from src.setup.create import create_database
from src.setup.migration import migrate
from src.setup.seed import seed_heroes, seed_patch

def build():
    """Creates databse, migrates, and seeds"""

    create_database()
    database = get_db()
    migrate(database)
    seed_patch(database)
    seed_heroes(database)
