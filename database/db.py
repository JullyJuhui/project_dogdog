from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 예시용 DB URL
DATABASE_URL = "postgresql+psycopg2://dog_5:kosmo@pg.nas6418.ddns.net:9934/Dogdog"
# DATABASE_URL = "postgresql+psycopg2://postgres:tiger@192.168.0.43:9934/Dogdog"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        