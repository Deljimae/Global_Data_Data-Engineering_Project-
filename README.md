# 🌍 Global Development Indicators Data Pipeline

This project builds an end-to-end data engineering pipeline that ingests, transforms, and analyzes key global development indicators such as:

- **Youth Literacy Rate**
- **GDP per Capita (PPP)**
- **Access to Electricity**
- **Under-5 Mortality Rate**
- **Renewable Energy Consumption**

These indicators are sourced from the World Bank and other open data repositories to support insights on global human development and infrastructure gaps.

---

## 🚀 Tech Stack

| Tool            | Role                                |
|-----------------|--------------------------------------|
| **Kestra**      | Workflow orchestration               |
| **AWS S3**      | Data lake (raw & processed data)     |
| **AWS Athena**  | Serverless SQL querying              |
| **Apache Iceberg** | Optimized table format for Athena |
| **dbt**         | Data transformation and modeling     |
| **Docker & EC2**| Infrastructure and environment setup |

---


## 🔄 ETL Pipeline
### 1️⃣ Data Ingestion – Python Script
Data fetched via World Bank API using:
```python
url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=10000"
response = requests.get(url)
...
df.to_csv("data/raw/{indicator_name}.csv")
```

### 2️⃣ Cloud Storage – AWS S3
- **Bucket**: `s3://deljimae-kestra-bucket/raw/global_data/`
- Uploads handled through Kestra orchestration flows

### 3️⃣ Transformation – dbt
- Created sources, staging, and models folders
- Removed rows with:
  - Null values
  - Non-country region codes (e.g. `'ZF'`, `'ZH'`)
- Generated final clean view: `vw_global_indicators_clean`
- **dbt Tests**:
  - `not_null`
  - `accepted_values`
  - Unique constraints
- Validated year, value, and country consistency

### 4️⃣ Data Warehouse – AWS Athena
- Tables registered via Iceberg-compatible external tables
- **Partitions**: by `year`
- All transformations accessible via `vw_global_indicators_clean`

## 📊 Power BI Dashboard
### Dashboard Pages:
1. **The Big Picture**  
   - Map view by country
   - KPI cards: Total indicators, country count, year range
   - Line chart: Global average trend over years
   - Slicers: `indicator_name`, `year`
[View Page 1](screenshots/page1_big_picture.png) 

2. **Compare Countries**  
   - Bar chart: Compare countries for selected metric
   - Line chart: Country trend across time
   - KPI cards: Max, Min, Average, Country Count
   - Slicers: `indicator_name`, `year`, `country_name`
[View Page 2](screenshots/page2_compare_countries.png) 

3. **Track an Indicator**  
   - Trend line chart: Country trend over years
   - Column chart: Year snapshot across countries
   - **Dynamic Titles via DAX**:  
     `"Compare Countries – " & SELECTEDVALUE(indicator_name) & " in " & SELECTEDVALUE(year)`
[View Page 3](screenshots/page3_track_indicators.png) 


## 🐞 Data Quality Gaps
- Several countries (e.g., Nigeria, Lebanon) missing in raw dataset
- Filtered non-country codes:  
  `'ZH'`, `'ZF'`, `'ZG'`, `'ZI'`, `'1A'`, `'V2'`, `'S3'`  

## 🧠 Learning Outcomes
- Using World Bank API programmatically
- Automating ingestion with Kestra
- Cleaning and testing data using dbt
- Creating Athena Iceberg tables and views
- Building dynamic, interactive Power BI dashboards
- Structuring documentation and GitHub workflows

## 📂 Project Structure

```bash
├── kestra/                 # Kestra flows for data orchestration
├── dbt/                    # dbt project (models, seeds, etc.)
├── data/                   # Local data staging (optional)
├── docker-compose.yml      # For Kestra containerized deployment
└── README.md
```
---

## 🧪 Indicators Tracked

```
indicators = [
    {"code": "SE.ADT.1524.LT.ZS", "name": "Youth Literacy Rate"},
    {"code": "NY.GDP.PCAP.PP.CD", "name": "GDP per Capita PPP"},
    {"code": "EG.ELC.ACCS.ZS", "name": "Access to Electricity"},
    {"code": "SH.DYN.MORT",       "name": "Under-5 Mortality Rate"},
    {"code": "EG.FEC.RNEW.ZS",    "name": "Renewable Energy Consumption"},
]
```
## ⚙️ How It Works
Ingestion: Kestra orchestrates workflows to extract indicator data from World Bank API.

Storage: Raw data is stored in AWS S3 and registered in Iceberg tables.

Transformation: dbt performs data cleaning, reshaping, and model creation.

Querying: Data is queried via Athena with partitioning and schema evolution.

Visualization (optional): Clean data can be visualized using tools like Looker or Tableau.

## 📈 Use Cases
Track Sustainable Development Goals (SDGs)

Compare development progress across countries or regions

Empower NGOs, researchers, and journalists with clean datasets


## Data Limitations

This project relies on publicly available global development indicators sourced from the World Bank.

Due to data coverage limitations, certain countries are missing from the raw dataset. These include, but are not limited to:

- **Africa**: Nigeria, Libya
- **Asia**: Malaysia, Qatar, North Korea
- **Europe**: Liechtenstein, Monaco
- **Others**: Tuvalu, Vatican City, Palau

These countries either lack recorded data for the selected indicators, have missing values across all years, or are aggregated under regional codes (e.g., ZH, ZF, XE).

> ⚠️ This is a known limitation of global socioeconomic datasets. The analysis presented is based only on the available data.


## 🛡️ Disclaimer
This project is for educational and demonstration purposes. The indicator data comes from public sources like data.worldbank.org.



## 👤 Author
**Ayodeji Lana**  
Computer Engineering Graduate | Data Engineering & Analytics Enthusiast  
🇳🇬 Nigeria  
LinkedIn: www.linkedin.com/in/ayodeji-lana-17a342267

*Tools: AWS, dbt, Power BI, Python, Kestra, Athena*  
🚀 *Ready to transition into LLM Zoomcamp after completing this end-to-end analytics pipeline!*
