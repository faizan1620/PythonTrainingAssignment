from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()


class Config(BaseModel):
    db_user: str
    db_password: str
    db_server: str
    db_name: str


Config.db_user = os.environ.get('DB_USER')

Config.db_password =  os.environ.get('DB_PASSWORD')

Config.db_server = os.environ.get('DB_SERVER')

Config.db_name = os.environ.get('DB_Name')

print(Config, Config.db_user)