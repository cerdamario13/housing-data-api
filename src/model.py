import wrangles
import pandas as pd
from config import mongo_config
from globals import pi_ws, pi_cell_range, metro_affordability_ws, metro_affordability_cell_range

# Read the sheet data


def _preprocess_data(data: dict) -> dict:
    """
    Preprocess data by converting years to list of dictionaries. Fluent UI Charts require data in this format
        [ { x: year, y: value }, ... ]
    """
    year_data = [{'x': val[0], 'y': val[1]} for val in data.items()]
    return year_data


def read_house_pi(location) -> list[dict]:
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
        query: {Metro Name: "${LOCATION}"}
    """
    try:
        data = wrangles.recipe.run(
        recipe=recipe,
        variables={
            "MONGO_USER": mongo_config.mongo_user,
            "MONGO_PASSWORD": mongo_config.mongo_password,
            "MONGO_HOST": mongo_config.mongo_host,
            "MONGO_DB_NAME": mongo_config.mongo_db_name,
            "MONGO_COLLECTION": mongo_config.mongo_collection,
            "LOCATION": location,
        }
        ).to_dict(orient='records')

        data = [_preprocess_data(x) for x in data]

        return data
    except:
        raise

def read_house_pi_xl(location):
    """
    Read the data from local xl file
    """

    # Extract cell values from range
    data = pi_ws[pi_cell_range]
    data_values = [[cell.value for cell in row] for row in data]

    # Convert to DataFrame
    headers = data_values[0]
    rows = data_values[1:]
    df = pd.DataFrame(rows, columns=headers)
    mask = df['Metropolitan Area'] == location
    pi_data = df[mask]

    if len(pi_data):
        data = pi_data.iloc[:, 2:].to_dict('records')[0]
        return _preprocess_data(data)
        
    else:
        return {"Error": "Query returned no data"}
    
def read_home_affordability_2022(location):
    """
    Get Metro Area-Typical Home Value and Mortgage Affordability: April 2022
    """

    # Extract cell values from range
    data = metro_affordability_ws[metro_affordability_cell_range]
    data_values = [[cell.value for cell in row] for row in data]

    # Convert to dataFrame
    headers = data_values[0]
    rows = data_values[1:]
    df = pd.DataFrame(rows, columns=headers)
    mask = df['Metropolitan Area'] == location
    m_f_data = df[mask]

    if len(m_f_data):
        # Do not need the 1, 2, and 3 columns
        data = m_f_data.iloc[:, 2:].to_dict('records')[0]
        return _preprocess_data(data)
    else:
        return {"Error": "Query returned no data"}
    


