from db import NetworkDB
from dotenv import load_dotenv
import os
load_dotenv()

URI = os.getenv('NEO4J_URI')
USER = os.getenv('NEO4J_USER')
PASSWORD = os.getenv('NEO4J_PASSWORD')

if __name__ == "__main__":
    db = NetworkDB(URI, USER, PASSWORD)



