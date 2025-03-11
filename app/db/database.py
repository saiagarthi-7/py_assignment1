from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
DB = os.getenv('SQLALCHEMY_DATABASE_URL', "postgresql://postgres:root@localhost/employee_db")

engine = create_engine(DB)
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()