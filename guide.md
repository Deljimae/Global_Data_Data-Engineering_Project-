# 🌍 Global Development Indicators Pipeline

## 📦 Prerequisites
| Requirement               | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Python 3.9+**           | Used to fetch World Bank data                                               |
| **AWS Account**           | S3 for data lake, Athena for querying                                       |
| **dbt Cloud**             | For transformation and modeling                                             |
| **Kestra**                | Orchestrating upload to S3 and Athena table creation                        |
| **Power BI Desktop**      | Building interactive dashboards                                             |
| **Athena ODBC Driver**    | Required for Power BI ↔️ Athena connection                                 |

## 🌐 Project Architecture
![Pipeline Architecture](assets/architecture.png)

## 📁 Folder Structure
```bash
global-indicators/
├── ingestion/                  # Python script to pull indicators from API
│   └── fetch_indicators.py
├── kestra_flows/               # YAMLs for S3/Athena table creation
│   └── global_data_ingestion.yml
├── data/
│   └── raw/                    # Output folder for CSVs
├── dbt/                        # dbt Cloud project folder
│   ├── models/
│   ├── snapshots/
│   ├── seeds/
│   └── dbt_project.yml
├── powerbi/
│   └── Global_Indicators.pbix
├── assets/                     # Architecture diagrams & screenshots
├── docs/                       # Documentation
├── README.md
└── guide.md                    # This file
```

🚀 Implementation Guide
✅ Step 1: Download Data from World Bank API
Run the script to fetch indicators:

```
cd ingestion/
python fetch_indicators.py
```

Output Format (data/raw/ files):

``` sql
country_code | country_name | year | value

```

## ✅ Step 2: Upload to S3 & Create Athena Tables with Kestra
1. Start Kestra via Docker:

```
docker run -p 8080:8080 kestra/kestra:latest
```
2. Access Kestra UI:
Open http://localhost:8080 in your browser

3. Upload the flow:

```
kestra_flows/global_data_ingestion.yml
```
Flow Actions:

- Uploads raw/*.csv to S3 bucket

- Creates external tables in Athena

- Formats tables for dbt consumption

## ✅ Step 3: Transform with dbt Cloud
Setup:

- Create dbt Cloud project connected to Athena

- Define sources for Athena tables

## 🛠️ Create Models

```sql
-- models/stg_global_indicators.sql
SELECT 
    country_code,
    country_name,
    year,
    value
FROM {{ source('worldbank', 'raw_indicators') }}
WHERE country_code NOT IN ('ZH','ZF','ZG','ZI','1A','V2','S3')

-- models/vw_global_indicators_clean.sql
{{
    config(
        materialized='view'
    )
}}
SELECT *
FROM {{ ref('stg_global_indicators') }}
WHERE value IS NOT NULL
```

## ✅ Add Data Tests

### models/schema.yml
version: 2
``` yaml
models:
  - name: stg_global_indicators
    tests:
      - not_null:
          column_name: country_code
      - accepted_values:
          column_name: country_code
          values: ['AF','AL','DZ', ...] # Valid ISO codes
      - unique:
          column_name: id

```
🚀 Run Job
Materialize final view: vw_global_indicators_clean ✅

## ✅ Step 4: Connect Athena to Power BI via ODBC

1. Download & install the Athena ODBC Driver

### In Power BI:
- Choose **ODBC** as data source  
- Select your **Athena DSN**  
- Navigate to your database and select `vw_global_indicators_clean`  
- Import the table into Power BI and start visualizing  

---

## 📊 Dashboard Pages

Inside Power BI (`Global_Indicators.pbix`), you’ll find:

| Page                     | Description                                      |
|--------------------------|--------------------------------------------------|
| **Page 1: Big Picture**  | KPIs, map, global time trend                    |
| **Page 2: Compare Countries** | Country bar chart + yearly trend line     |
| **Page 3: Track an Indicator** | Line + column charts for a specific country and metric |

---

## 📁 Supporting Assets

- `/assets/architecture.png`: Pipeline architecture  
- `/docs/Global_Data_PowerPoint.pdf`: Final dashboard export  
- `/screenshots/`: Dashboard views per page (optional)  

---

## 🧪 Troubleshooting

| Issue                         | Fix                                                                 |
|------------------------------|----------------------------------------------------------------------|
| **ODBC not working**         | Confirm AWS credentials & region match Athena settings              |
| **Missing countries in dashboard** | Check dbt transformation for filters and `NULL` handling      |
| **Power BI visual interaction broken** | Use **“Edit Interactions”** under Visual Format options  |

