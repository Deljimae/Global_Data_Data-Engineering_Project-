-- models/dimensions/dim_country.sql

select distinct
  country_code,
  country_name
from {{ ref('stg_kestradb__global_indicators_ext') }}
where country_code not in ('ZH', 'ZF', 'ZG')
