import pandas as pd

def gistemp_fetch():
    df = pd.read_csv('https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv' , skiprows = 1)

    dataFrame = pd.DataFrame(df)

    return dataFrame

 
