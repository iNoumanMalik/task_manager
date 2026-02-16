from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine( 
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(bind = engine, autoflush=False,autoCommit=False)

# Foundation of ORM Models
# Keep track of all models
# Provide metadata like tables, columns and relationships
Base = declarative_base()

# provides db session to the rest of application and the finally block ensures the session is closed, preventing leaks. 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()