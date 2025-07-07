Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test

## 🔧 dbt Project: Global Indicator Analytics

This subproject contains our dbt transformation pipeline, modeling global development indicators from raw CSVs stored in S3 into clean dimensional models for analytics in Power BI.

### 🌐 Data Source
- Source: World Bank Indicator CSVs (e.g., literacy rate, access to electricity)
- Storage: AWS S3
- Orchestration: Kestra
- Query Engine: Athena

### 🛠️ Transformations
- `stg_...` models: Raw → cleaned staging
- `dim_country`, `dim_indicator`: Dimension tables
- `fct_global_indicators`: Fact table of country-indicator values

### ✅ Tests Implemented
- Not null & accepted values on `year`, `value`
- Unique tests on country + indicator combinations

---

You can view the full dbt project under [`/dbt/Global_Data_DE_Project`](./dbt/Global_Data_DE_Project)


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](https://getdbt.com/community) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
