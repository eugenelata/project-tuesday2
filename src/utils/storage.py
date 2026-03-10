import pickle
from pathlib import Path
from ..models.address_book import AddressBook
from ..models.notebook import NoteBook

DATA_DIR = Path.home() / ".assistant"
DATA_FILE = DATA_DIR / "data.pkl"


def save_data(book, notebook):
    """TODO: serialize book and notebook to DATA_FILE using pickle."""
    pass


def load_data():
    """TODO: deserialize from DATA_FILE. Return (AddressBook, NoteBook).
    Create DATA_DIR if it doesn't exist. Return empty instances on FileNotFoundError.
    """
    pass
