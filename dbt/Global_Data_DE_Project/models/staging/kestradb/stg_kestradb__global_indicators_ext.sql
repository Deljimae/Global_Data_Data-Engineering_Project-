SELECT
  country_code,
  country_name,
  year,
  value,
  regexp_extract("$path", '[^/]+$', 0) AS filename
FROM {{ source('kestradb', 'global_indicators_ext') }}
WHERE value IS NOT NULL
  AND year IS NOT NULL
  AND country_code NOT IN ('ZH', 'ZF', 'ZG')
