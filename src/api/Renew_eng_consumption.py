import requests 
import pandas as pd

def renew_eng_consum( ):

 
    meta_url = (f'https://api.worldbank.org/v2/indicator/EG.FEC.RNEW.ZS?format=json')

    # since this api retun data in multiple pages so loopin through pages
    all_data = []
    page = 1
   

    print('Processing request...')
    while True:
        url = (f'https://api.worldbank.org/v2/country/ALL/indicator/EG.FEC.RNEW.ZS?format=json&per_page=2000&page={page}')
        r = requests.get(url , timeout = 20).json()
        
        total_pages = r[0]['pages']

        print(f"\rFetching page {page}/{total_pages}...", end='', flush=True)
        all_data.extend(r[1])
        if page >= r[0]['pages']:
            break
        else:
            page += 1
    print(f'\nDone. Collected {len(all_data)} records .')


     
    meta_response = requests.get(meta_url)
    metadata = meta_response.json()[1][0]

 # converting data into DataFrame
    print('converting into DataFrame')
    df = pd.DataFrame(all_data)        
    df = df[['date' , 'value' , 'countryiso3code' ,'country'  ]]
    df['country'] = df['country'].apply(lambda x: x.get('value') if isinstance(x, dict) else x)

# Renaming columns
    df = df.rename(columns = {'countryiso3code' : 'Country_code'})
    df = df.rename(columns = {'date' : 'year'})
    df = df.rename(columns = {'value' : 'total_renewable_energy(%)'})

# changing data types of columnms
    df['year'] = df['year'].astype(int)
    df['total_renewable_energy(%)'] = pd.to_numeric(df['total_renewable_energy(%)'] , errors = 'coerce')
    df['total_renewable_energy(%)'] = df['total_renewable_energy(%)'].astype(float)

    print('Got dataFrame shape :' , df.shape)

    return df ,metadata