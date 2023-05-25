from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(self, db_user: str, db_password: str, db_server: str, db_name: str):
        self.db_user = db_user
        self.db_password = db_password
        self.db_server = db_server
        self.db_name = db_name


db_user = os.environ.get("DB_USER", "")
db_password = os.environ.get("DB_PASSWORD", "")
db_server = os.environ.get("DB_SERVER", "localhost")
db_name = os.environ.get("DB_Name", "student")

config = Config(db_user, db_password, db_server, db_name)
