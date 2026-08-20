import requests 
import pandas as pd

def renew_eng_consum(country_code ):

# | Indicator Code           | Description                            | Unit |
# |
# | ``EN.GHG.CO2.MT.CE.AR5`` | Total CO₂ emissions (excluding LULUCF) | Mt CO₂e |
# | ``EN.GHG.CO2.PC.CE.AR5`` | CO₂ emissions per capita (excluding LULUCF) | t CO₂e per person |

    url = (f'https://api.worldbank.org/v2/country/{country_code}/indicator/EG.FEC.RNEW.ZS?format=json&per_page=500')
    meta_url = (f'https://api.worldbank.org/v2/indicator/EG.FEC.RNEW.ZS?format=json')
    response = requests.get(url)
    meta_response = requests.get(meta_url)

    raw = response.json()
    metadata = meta_response.json()[1][0]
    data = raw[1] 

    df = pd.DataFrame(data)
    df = df[['date' , 'value' , 'countryiso3code']]
    df = df.rename(columns = {'countryiso3code' : 'Country_code'})
    df['date'] = df['date'].astype(int)
    df['value'] = df['value'].astype(float)

    return df , metadata