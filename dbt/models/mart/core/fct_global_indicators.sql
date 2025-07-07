SELECT
  s.country_code,
  c.country_name,
  s.year,
  s.value,
  d.indicator_id,
  d.indicator_name
FROM {{ ref('stg_kestradb__global_indicators_ext') }} s
LEFT JOIN {{ ref('dim_country') }} c
  ON s.country_code = c.country_code
LEFT JOIN {{ ref('dim_indicator') }} d
  ON REGEXP_EXTRACT(s.filename, '[^/]+$', 0) = d.indicator_id || '.csv'
WHERE s.value IS NOT NULL
  AND s.year IS NOT NULL
  AND s.country_code NOT IN ('ZH', 'ZF', 'ZG')
