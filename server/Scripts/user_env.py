from dotenv import load_dotenv
import os
load_dotenv()

class env:
    def __init__(self,PORT=os.getenv('SERVER_PORT'),MYSQL_URL=os.getenv('MYSQL_URL'),
                 MYSQL_PORT=os.getenv('MYSQL_PORT'),MYSQL_DATA_BASE=os.getenv('MYSQL_DATA_BASE'),
                 MYSQL_TABLE_NAME=os.getenv('MYSQL_TABLE_NAME'),MYSQL_USER=os.getenv('MYSQL_USER'),
                 MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')):
        self.SERVER_PORT= PORT
        self.MYSQL_URL = MYSQL_URL
        self.MYSQL_PORT=MYSQL_PORT
        self.MYSQL_DATA_BASE=MYSQL_DATA_BASE
        self.MYSQL_TABLE_NAME=MYSQL_TABLE_NAME
        self.MYSQL_USER=MYSQL_USER
        self.MYSQL_PASSWORD=MYSQL_PASSWORD