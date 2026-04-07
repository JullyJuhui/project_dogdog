from sqlalchemy import select
from sqlalchemy.orm import Session

from database.db import Product, Product_Detail

def get_product_list(db: Session, keyword: str | None = None):
    query = (
        select(Product.product_id, 
               Product.product_detail_id, 
               Product_Detail.product_name, 
               Product.weight,
               Product.active
               )
        # .options(joinedload(Product.product_detail))
        .join(Product_Detail, Product.product_detail_id == Product_Detail.product_detail_id)
        .where(Product.active == True)
    )

    if keyword is not None and keyword.strip() != "": # 키워드가 있을때
        query = query.where(Product_Detail.product_name.ilike(f"%{keyword.strip()}%"))

    result = db.execute(query)
    # products = result.scalars().all()
    products = result.all()

    return products