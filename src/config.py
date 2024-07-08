import os

class monog_db():
    mongo_user = os.getenv("MONGO_USER", "...")
    mongo_password = os.getenv("MONGO_PASSWORD", "...")
    mongo_collection = os.getenv("MONGO_COLLECTION", "...")
    mongo_host = os.getenv("MONGO_HOST", "...")