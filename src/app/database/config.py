import os

user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
db_name = os.getenv("DB_NAME")
domain = os.getenv("MONGO_DOMAIN")

class Config:
    MONGO_URI = os.getenv(
        "MONGO_URI",
        f"mongodb://{user}:{password}@{domain}:27017/{db_name}?authSource=admin"
    )
