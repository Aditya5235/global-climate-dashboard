import pandas as pd
import requests

def get_precipitation( ):

    # sincce this API returns data per pages , so looping through pages
    
    data = []
    page = 1

    print("Processing request..")
    while True:  
       
       url = (f"https://api.worldbank.org/v2/country/all/indicator/AG.LND.PRCP.MM?format=json&per_page=20000&page={page}")

       r = requests.get(url , timeout = 5).json()
    
       

       total_pages = r[0]['pages']
       print(f"\rFetching page {page}/{total_pages}...", end='', flush=True)
      
       data.extend(r[1])
       if page >= r[0]['pages']:
           break
       else:
           page += 1;

    print(f'\nDone. Collected {len(data)} records.')

    print('Converting into dataFrame')
    df= pd.DataFrame(data)
    df = df[[ 'date' ,'countryiso3code','value' , 'country']]
    df['country'] = df['country'].apply(lambda x: x.get('value') if isinstance(x,dict) else x)

# Renaming columns
    df = df.rename(columns = {'countryiso3code' : 'Country_code'})
    df = df.rename(columns = {'date' : 'year'})
    df = df.rename(columns = {'value' :"annual_precipitation_mm"})

    return  df
