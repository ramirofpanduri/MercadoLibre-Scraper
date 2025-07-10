from models import Base
from db import engine


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
