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
