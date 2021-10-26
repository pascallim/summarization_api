from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER_NAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
DB_NAME_PG = 'squirro_db'

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_NAME_PG}:{PASSWORD_PG}@127.0.0.1/{DB_NAME_PG}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
