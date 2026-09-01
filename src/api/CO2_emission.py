import requests 
import pandas as pd

def co2_emission():

# | Indicator Code           | Description                            | Unit |
# |
# | ``EN.GHG.CO2.MT.CE.AR5`` | Total CO₂ emissions (excluding LULUCF) | Mt CO₂e |
# | ``EN.GHG.CO2.PC.CE.AR5`` | CO₂ emissions per capita (excluding LULUCF) | t CO₂e per person |

    # fatching Total Co2 emission
    url = (f"https://api.worldbank.org/v2/country/all/indicator/EN.GHG.CO2.MT.CE.AR5?format=json&per_page=20000")
    meta_url = (f'https://api.worldbank.org/v2/indicator/EN.GHG.CO2.MT.CE.AR5?format=json')
    response = requests.get(url , timeout = 20)
    meta_response = requests.get(meta_url)

    raw = response.json()
    metadata = meta_response.json()[1][0]
    data = raw[1] 

# extracting usefull data for Total Co2 emission

    total_em = pd.DataFrame(data)

    total_em = total_em[['date' , 'value' , 'countryiso3code']]
    
    total_em = total_em.rename(columns = {'countryiso3code' : 'Country_code'})
    total_em = total_em.rename(columns = {'value' : 'T_CO₂_emi(in mt)'})

    total_em['date'] = total_em['date'].astype(int)
    total_em['T_CO₂_emi(in mt)'] = total_em['T_CO₂_emi(in mt)'].astype(float)

    # fatching Per_capita Co2 emission

    url = (f"https://api.worldbank.org/v2/country/all/indicator/EN.GHG.CO2.PC.CE.AR5?format=json&per_page=20000")
    response = requests.get(url ,timeout = 20)    

    raw = response.json() 
    data = raw[1] 

    per_capita_em = pd.DataFrame(data)

    per_capita_em = per_capita_em[ ['date' , 'value' , 'countryiso3code'] ] 

    per_capita_em['value'] = per_capita_em['value'].astype(float)
    per_capita_em['date'] = per_capita_em['date'].astype(int)

    per_capita_em = per_capita_em.rename(columns ={'value':'Co2_per_capita(in ton)'})
    per_capita_em = per_capita_em.rename(columns = {'countryiso3code' : 'Country_code'})
    
    # concating percapita data with total co2 emission

    df = pd.merge(total_em , per_capita_em ,  on =['Country_code', 'date'])
   

   

    return df , metadata  


