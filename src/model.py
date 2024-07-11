import wrangles
import pandas as pd
from config import mongo_config

def read_house_pi():
    """
    Read house price to income ratio data
    """
    recipe = """
    read:
    - mongodb:
        user: ${MONGO_USER}
        password: ${MONGO_PASSWORD}
        database: ${MONGO_DB_NAME}
        collection: ${MONGO_COLLECTION}
        host: ${MONGO_HOST}
        projection: {_id: 0}
    """

    data = wrangles.recipe.run(
    recipe=recipe,
    variables={
        "MONGO_USER": mongo_config.mongo_user,
        "MONGO_PASSWORD": mongo_config.mongo_password,
        "MONGO_HOST": mongo_config.mongo_host,
        "MONGO_DB_NAME": mongo_config.mongo_db_name,
        "MONGO_COLLECTION": mongo_config.mongo_collection
    }
    ).to_dict(orient='records')

    return data

