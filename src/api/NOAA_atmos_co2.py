import requests
import pandas as pd
from io import StringIO


def atmospheric_co2():

    url =  (f'https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv')

    response = requests.get(url)
    response.raise_for_status()

    data = response.text.splitlines()[40:]
    
    df = pd.read_csv(StringIO("\n".join(data)))
    
     
     
    return df