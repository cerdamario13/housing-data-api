import os

class mongo_config():
    mongo_user = os.getenv("MONGO_USER", "...")
    mongo_password = os.getenv("MONGO_PASSWORD", "...")
    mongo_host = os.getenv("MONGO_HOST", "...")
    mongo_db_name= os.getenv("MONGO_DB_NAME", "...")
    mongo_collection = os.getenv("MONGO_COLLECTION", "...")
    