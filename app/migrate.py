from database import get_session

from models import Category, Product
from utils import load_data


with get_session() as session:
    categories = load_data(filename="categories.json")

    # for item in categories:
    #     ins = Category(name=item['name'])

    #     session.add(ins)

    products = load_data(filename="products.json")

    for item in products:
        ins = Product(
            title=item["title"],
            description=item["description"],
            price=item["price"],
            category_id=item["category_id"],
        )

        session.add(ins)

    session.commit()
