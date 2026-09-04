import requests
import pandas as pd

def get_country_classification():
    """
    Pulls the World Bank's own country/aggregate classification.
    Returns a dataframe: Country_code, is_aggregate (bool), region
    """
    url = "https://api.worldbank.org/v2/country?format=json&per_page=400"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    _, records = resp.json()

    rows = []
    for r in records:
        rows.append({
            "Country_code": r["id"],  # ISO3 code
            "region": r["region"]["value"],
            "is_aggregate": r["region"]["value"] == "Aggregates"
        })
    return pd.DataFrame(rows)

classification = get_country_classification()
classification.to_csv('data/reference/country_classification.csv', index=False) 
 