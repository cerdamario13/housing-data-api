import wrangles
import pandas as pd
from config import mongo_config
from globals import *

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

    # clean up the name
    if location == "Austin-Round Rock, TX":
        location = "Austin-Round Rock-Georgetown, TX"

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
        data = m_f_data.to_dict('records')[0]
        return data
    else:
        return {"Error": "Query returned no data"}
    
def year_to_year_change(location):
    """
    Get the year to year change for rent and home value
    """

    if location == 'Austin-Round Rock, TX':
        location = "Austin, TX"


    # Extract cell values from range
    data = yoy_change_ws[yoy_change_cell_range]
    data_values = [[cell.value for cell in row] for row in data]
    
    headers = data_values[0]
    rows = data_values[1:]
    df = pd.DataFrame(rows, columns=headers)
    # reset the index
    mask = df['Metropolitan Area'] == location
    m_f_data = df[mask]

    # Rent values
    rent_keys = list(m_f_data.iloc[0].index)[1:8]
    rent_values = list(m_f_data.iloc[0].values)[1:8]
    rent_dict = [{k:float(v)} for (k,v) in zip(rent_keys, rent_values)]

    # House Values
    house_keys = list(m_f_data.iloc[0].index)[8:]
    house_values = list(m_f_data.iloc[0].values)[8:]
    house_dict = [{k:float(v)} for (k,v) in zip(house_keys, house_values)]

    data = {
        'rent_data': rent_dict,
        'house_data': house_dict
    }

    if len(m_f_data):
        return data
    else:
        return {"Error": "Query returned no data"}

