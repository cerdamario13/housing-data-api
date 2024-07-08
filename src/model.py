import wrangles
import pandas as pd

def read_house_pi():
    """
    Read house price to income ratio data
    """
    recipe = """
    read:
    - mongodb:
        user: ${MONGO_USER}
        password: ${MONGO_PASSWORD}
        database: ${MONGO_DB}
        collection: ${MONGO_COLLECTION}
        host: ${MONGO_HOST}
    """

    data = wrangles.recipe.run(
    recipe=recipe,
    ).to_dict(orient='records')

    return data

