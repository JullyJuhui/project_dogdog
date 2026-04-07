from sqlalchemy.orm import Session
from sqlalchemy import select
from database.db import Product


def get_product_list(db: Session, keyword: str | None = None):
    query = select(Product).where(Product.active == True)

    if keyword and keyword.strip():
        query = query.where(Product.product_name.ilike(f"%{keyword.strip()}%"))

    result = db.execute(query)
    products = result.scalars().all()

    return products