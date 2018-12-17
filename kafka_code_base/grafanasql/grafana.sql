-- Trip:

SELECT
  base.time,
  case
  when p.value is null then 0
  else p.value
  end
FROM
  (
    SELECT
      time,
      user_id
    FROM generate_series(($__unixEpochFrom()/600)::int*600,($__unixEpochTo()/600)::int*600,600) as times(time),
    (SELECT distinct request_time_stamp from trip_request_data_entries) as user_id
  ) as base
  LEFT OUTER JOIN (
    SELECT
      $__timeGroup(request_time_stamp,'-10m') as time,
      COUNT(user_id) as value

    FROM trip_request_data_entries
    WHERE $__timeFilter(request_time_stamp)
       GROUP BY 1
       ORDER BY 1
  ) as p ON (p.time = base.time) ORDER BY 1,2;



-- DriverPing:

SELECT
  base.time,
  case
  when p.value is null then 0
  else p.value
  end
FROM
  (
    SELECT
      time,
      driver_id
    FROM generate_series(($__unixEpochFrom()/600)::int*600,($__unixEpochTo()/600)::int*600,600) as times(time),
    (SELECT distinct driver_id from driver_ping_info) as driver_id
  ) as base
  LEFT OUTER JOIN (
    SELECT
      $__timeGroup(update_time,'-10m') as time,
      COUNT(driver_id) as value

    FROM driver_ping_info
    WHERE $__timeFilter(update_time)
       GROUP BY 1
       ORDER BY 1
  ) as p ON (p.time = base.time) ORDER BY 1,2;
