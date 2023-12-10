import os

from dotenv import load_dotenv

load_dotenv()


class ProductionConfig:
    server = os.getenv('POSTGRES_HOST')
    port = 5432
    database = os.getenv('POSTGRES_DATABASE')
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
     






