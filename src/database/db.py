from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = ""

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
