import requests
import pandas as pd
from io import StringIO


def atmospheric_co2():

    url =  (f'https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv')

    response = requests.get(url)
    response.raise_for_status()

    data = response.text.splitlines()[40:]
    x = response.text.splitlines()[:40]
    last_update = ''
    for i in x:
     
     if "File Creation" in i:
      last_update = i
      break
    
    df = pd.read_csv(StringIO("\n".join(data)))
    
     
     
    return df , last_update