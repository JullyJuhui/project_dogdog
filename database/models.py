from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# 일단 필요한 컬럼들만 넣어놓음.
# OPD
Base = declarative_base()

class ProductDetail(Base):
    __tablename__ = "product_detail"
    __table_args__ = {"schema":"OPD"}

    product_detail_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)

class Product(Base):
    __tablename__ = "product"
    __table_args__ = {"schema":"OPD"}

    product_id = Column(Integer, primary_key=True, index=True)
    product_detail_id = Column(Integer, ForeignKey("OPD.product_detail.product_detail_id"), nullable=False)
    weight = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    
    product_detail = relationship("ProductDetail")
    # product_detail = relationship("ProductDetail", back_populates="products")