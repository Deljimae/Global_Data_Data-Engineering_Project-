SELECT DISTINCT
  split_part(filename, '.', 1) AS indicator_id,
  replace(split_part(filename, '.', 1), '_', ' ') AS indicator_name
FROM {{ ref('stg_kestradb__global_indicators_ext') }}
