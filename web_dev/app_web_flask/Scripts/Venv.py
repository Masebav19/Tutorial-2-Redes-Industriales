from dotenv import load_dotenv
import os
load_dotenv()

class env: 
    def __init__(self,
                 PORT = os.getenv("APP_PORT")):
        self.PORT= PORT