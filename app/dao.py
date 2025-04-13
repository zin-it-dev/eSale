from database import get_session
from models import Category

session = get_session()


def load_categories():
    return session.query(Category).filter(Category.is_active.is_(True)).all()
