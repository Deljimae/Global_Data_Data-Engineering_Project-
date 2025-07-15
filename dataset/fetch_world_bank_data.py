import requests
import pandas as pd
import os


def fetch_indicator(indicator_code, indicator_name, output_folder="data/raw"):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=10000"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

    json_data = response.json()

    if len(json_data) < 2:
        print(f"⚠️ No data found or error for indicator: {indicator_code}")
        print(f"🔎 API message: {json_data}")
        return

    records = json_data[1]  # Data is in the second item

    # Normalize into a flat table
    df = pd.json_normalize(records)
    df = df[["country.id", "country.value", "date", "value"]]
    df.columns = ["country_code", "country_name", "year", "value"]
    # Convert year to integer, handle missing values
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Save to CSV
    os.makedirs(output_folder, exist_ok=True)
    filename = f"{indicator_name.lower().replace(' ', '_')}.csv"
    filepath = os.path.join(output_folder, filename)
    df.to_csv(filepath, index=False)
    print(f"✅ {indicator_name} saved to {filepath}")

    return df

if __name__ == "__main__":
    indicators = [
        {"code": "SE.ADT.1524.LT.ZS", "name": "Youth Literacy Rate"},
        {"code": "NY.GDP.PCAP.PP.CD", "name": "GDP per Capita PPP"},
        {"code": "EG.ELC.ACCS.ZS", "name": "Access to Electricity"},
        {"code": "SH.DYN.MORT", "name": "Under-5 Mortality Rate"},
        {"code": "EG.FEC.RNEW.ZS", "name": "renewable_energy_consumption"},
    ]

    for ind in indicators:
        try:
            print(f"📡 Fetching: {ind['code']} ({ind['name']})")
            fetch_indicator(ind["code"], ind["name"])
        except Exception as e:
            print(f"❌ Error fetching {ind['name']}: {e}")
