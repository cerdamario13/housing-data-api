import wrangles
import pandas as pd
from config import mongo_config

def _preprocess_data(data: dict) -> dict:
    """
    Preprocess data by converting years to list of dictionaries. Fluent UI Charts require data in this format
    {
        x: year,
        y: value
    }
    """
    new_years = [{'x': val[0], 'y': val[1]} for val in data['years'].items()]
    data['years'] = new_years
    return data


def read_house_pi() -> list[dict]:
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
    
    data = [_preprocess_data(x) for x in data]

    return data

