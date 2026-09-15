# This module includes a function for calling the census API and downloading a requested ACS 5-yr variable.

from census_api_key import CENSUS_API_KEY # Copy or link this locally and make sure it is in .gitignore
import pandas as pd
import requests

def retrieve_acs_var(
    variables: dict, # dict mapping strings to read to friendly name strings for output. We'll need the full variable column
    # including the '_001E' etc.
    state_fips: str = '06', # default to CA
    acs_year: int = 2024,
    geo: str = 'county',
    base_url: str = 'https://api.census.gov/data/YYYY/acs/acs5', # should have a dummy YYYY to be replaced
    out_geo_name: str = 'GEOID',
    trim_geo: int = 9 # number of chars to remove from the beginning of the geos.
):
    """
    Retrieve an ACS variable using the census API.

    Parameters
    ----------
    variables : dictionary of variable names with full column suffix (i.e. '_001E')
    state_fips : FIPS code str for the state to retrieve, default = California '06'
    acs_year : 5-year ACS, default = 2024
    geo : geography level to retrieve, default = 'county'. state is not supported.
    Other optional args: base_url, out_geo_name, and trim_geo.

    Returns
    -------
    Dataframe with variables and metadata as columns, index = GEOID.

    Example usage
    -------------
    df = retrieve_acs_var({'B25040_001E': 'Total Occupied Homes', 'B25040_004E': 'Homes with Electric Heating'})

    """
    url = base_url.replace('YYYY', str(acs_year))
    print(f"Downloading from base URL: {url}")
    
    # params is a dictionary: a set of labeled values, like filling in a form
    params = {
        "for": geo + ":*",                        # every geo...
        "in": "state:" + state_fips,	          # ...in our state
        "key": CENSUS_API_KEY,
    }

    # for tracts and block groups we may need to clarify all counties
    if geo == 'block group':
        params['in'] = "state:" + state_fips + " county:*"
    
    # We'll define "get" by appending our variable list
    params['get'] = 'NAME,GEO_ID' # geo name and full FIPS
    
    for v in variables.keys():
        params['get'] += ',' + v # += concatenates for strings

    response = requests.get(url, params=params)      # requests.get is a function; url and params are its arguments
    print("Status code:", response.status_code)     # 200 means it worked
    
    # if it worked, keep the data; if not, print the Census Bureau's explanation instead of a scary traceback
    if response.status_code == 200:
        try:
            data = response.json()
            print(data[:3])                              # peek at the first three rows of what came back
        except requests.exceptions.JSONDecodeError:
            print("No valid data received from census API. Aborting.")
            return None
    else:
        print("The API said no. Check API_KEY and the variable names. The message it sent back:")
        print(response.text[:300])
        return None

    # The API returns a list of lists; the first row is the column headers
    
    df = pd.DataFrame(data[1:], columns=data[0])

    # Print the rename for reference:
    for v in variables.keys():
        if v in df.columns:
            print(f"Retrieved ACS variable {v}: renaming as {variables[v]}.")
        else:
            print(f"Failed to retrieve variable {v}. Aborting.")
            return None
    
    df = df.rename(variables, axis=1) # Rename to user-friendly names
    df['GEO_ID'] = df['GEO_ID'].map(lambda x: x[trim_geo:]) # Trim first 9 chars
    df = df.rename({'GEO_ID': out_geo_name}, axis=1) # Rename to user-friendly names

    # Default to outputting numeric values
    df[list(variables.values())] = df[list(variables.values())].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    # This syntax took a lot of trial and error!
    # For the list of columns matching values in the variable dictionary, apply the function pd.to_numeric.
    
    df = df.set_index(out_geo_name)

    print(df.head()) #head returns just the first 5 rows
    print(f"Retrieved {len(df)} rows in total.")
    
    return df


if __name__ == '__main__': # if this is running standalone for testing
    print('County:\n\n')
    df = retrieve_acs_var({'B25040_001E': 'Total Occupied Homes', 'B25040_004E': 'Homes with Electric Heating'})
    print(df.head())
    print(df.columns)

    print('Block Group:\n\n')
    df = retrieve_acs_var({'B25040_001E': 'Total Occupied Homes', 'B25040_004E': 'Homes with Electric Heating'},
                         geo="block group")
    print(df.head())
    print(df.columns)

    print('Tract:\n\n')
    df = retrieve_acs_var({'B25040_001E': 'Total Occupied Homes', 'B25040_004E': 'Homes with Electric Heating'},
                         geo="tract")
    print(df.head())
    print(df.columns)