
# import the required packages.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#mysql database connection
# sqlalchemyDatabaseUrl  = "mysql+pymysql://root:root@127.0.0.2:3306/mydb"

#sqlite
sqlalchemyDatabaseUrl = "sqlite:///./sql_app.db"

#postgresql
# sqlalchemyDatabaseUrl = "postgresql://user:password@postgresserver/db"

#Create engine instance
engine = create_engine(sqlalchemyDatabaseUrl)

#Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  create a Base class , use the function declarative_base() that returns a class
Base = declarative_base()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
        