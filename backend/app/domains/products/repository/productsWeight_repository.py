from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import Product

def get_product_weight(db: Session, keyword: int | None = None):
    query = (
        select(Product.product_id,  
                Product.weight,
                Product.active
                )
        # .options(joinedload(Product.product_detail))
        # .join(ProductDetail, Product.product_detail_id == ProductDetail.product_detail_id)
        .where(Product.active == True, Product.product_detail_id == Product.product_detail.product_detail_id)
    )

    # if keyword is not None and keyword.strip() != "": # 키워드가 있을때
    #     query = query.where(ProductDetail.product_name.ilike(f"%{keyword.strip()}%"))

    result = db.execute(query)
    # products = result.scalars().all()
    products = result.all()

    return products