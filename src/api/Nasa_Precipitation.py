import pandas as pd
import requests

def get_precipitation(start_dt , end_dt , lon , lat):

    url = (f"https://power.larc.nasa.gov/api/temporal/daily/point?start={start_dt}&end={end_dt}&latitude={lat}&longitude={lon}&community=ag&parameters=PRECTOTCORR&format=json&header=true")


    response = requests.get(url , timeout = 20)

    response.raise_for_status()

    data = response.json()
    
    coordinates = data['geometry']['coordinates']    

    coordinate_df = pd.DataFrame([coordinates ], columns = ['Latitude' , 'Longitude' , 'Elevation(in m)'])
    
    df = data['properties']['parameter']['PRECTOTCORR']
    precipation_df = pd.DataFrame( list(df.items()),
                                   columns = ["date", "precipitation"])

    return precipation_df , coordinate_df