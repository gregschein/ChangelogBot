from build import build
from src.setup.teardown import teardown_db

def reset():
    """Deletes old database, then creates, migrates, and seeds"""
    teardown_db()
    build()

if __name__ == '__main__':
    reset()
