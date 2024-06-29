from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/myweb"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)