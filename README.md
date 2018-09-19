# StatsBomb JSON parser

[![PyPI version](https://badge.fury.io/py/statsbomb.svg)](https://pypi.org/project/statsbomb/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/statsbomb.svg)
[![Build Status](https://travis-ci.org/imrankhan17/statsbomb-parser.svg?branch=master)](https://travis-ci.org/imrankhan17/statsbomb-parser)
[![codecov](https://codecov.io/gh/imrankhan17/statsbomb-parser/branch/master/graph/badge.svg)](https://codecov.io/gh/imrankhan17/statsbomb-parser)
[![HitCount](http://hits.dwyl.io/imrankhan17/statsbomb.svg)](http://hits.dwyl.io/imrankhan17/statsbomb)

Convert competitions/matches/lineups/events JSON data released by [StatsBomb](https://github.com/statsbomb/open-data) into easy-to-use CSV format.

## Installation

`$ pip install statsbomb`

## Example usage

 * Parsing the `competitions.json` file:

```python
import statsbomb as sb

comps = sb.Competitions()
print(len(comps))  # 3
json_data = comps.data  # underlying json data

df = comps.get_dataframe()
print(df)
```

| competition_id | competition_name        | country_name             | match_available            | match_updated              | season_id | season_name |
|----------------|-------------------------|--------------------------|----------------------------|----------------------------|-----------|-------------|
| 37             | FA Women's Super League | England                  | 2018-09-08T07:33:39.356340 | 2018-09-08T07:33:39.356340 | 1         | 2017/2018   |
| 43             | FIFA World Cup          | International            | 2018-09-08T07:33:39.356340 | 2018-09-08T14:30:04.356514 | 3         | 2018        |
| 49             | NWSL                    | United States of America | 2018-09-08T07:33:39.356340 | 2018-09-08T07:33:39.356340 | 3         | 2018        |


 * Parsing an events json file to extract shots:

```python
import statsbomb as sb

events = sb.Events(event_id='8658')
df = events.get_dataframe(event_type='shot')
print(len(df))  # 23

print(df)
```

| event_type | id                                   | index | period | timestamp    | minute | second | possession | possession_team | play_pattern   | off_camera | team    | player            | position             | duration | under_pressure | statsbomb_xg | key_pass_id                          | body_part | type      | outcome | technique   | first_time | follows_dribble | redirect | one_on_one | open_goal | deflected | start_location_x | start_location_y | end_location_x | end_location_y | end_location_z |
|------------|--------------------------------------|-------|--------|--------------|--------|--------|------------|-----------------|----------------|------------|---------|-------------------|----------------------|----------|----------------|--------------|--------------------------------------|-----------|-----------|---------|-------------|------------|-----------------|----------|------------|-----------|-----------|------------------|------------------|----------------|----------------|----------------|
| shot       | c3ffbb5f-d836-4d33-a02a-3a994990d253 | 577   | 1      | 00:20:51.227 | 20     | 51     | 39         | Croatia         | From Free Kick | False      | Croatia | Domagoj Vida      | Left Center Back     | 1.013    |                | 0.05478843   | baafd0a9-1031-46df-82a2-16538d6e94cf | Head      | Open Play | Off T   | Normal      |            |                 |          |            |           |           | 112.0            | 49.0             | 119.0          | 36.7           | 4.7            |
| shot       | d7a727de-1b60-47c7-b9fa-10948bb730ed | 634   | 1      | 00:23:34.907 | 23     | 34     | 45         | Croatia         | From Free Kick | False      | Croatia | Ivan Rakitić      | Left Center Midfield | 2.053    |                | 0.04375982   | 9cc48e31-5a52-4074-97b1-5c3eafdd753d | Left Foot | Open Play | Off T   | Volley      |            |                 |          |            |           |           | 108.0            | 29.0             | 120.0          | 46.9           | 6.1            |
| shot       | 20bcdb94-9507-4bed-8315-edddcbb84081 | 736   | 1      | 00:27:53.880 | 27     | 53     | 53         | Croatia         | From Free Kick | False      | Croatia | Ivan Perišić      | Left Wing            | 0.587    |                | 0.12172278   | 90fdf286-3e32-4646-bcb1-a83a7d51593f | Left Foot | Open Play | Goal    | Half Volley |            | True            |          |            |           | True      | 105.0            | 32.0             | 120.0          | 43.3           | 0.7            |
| ...        | ...                                  | ...   | ...    | ...          | ...    | ...    | ...        | ...             | ...            | ...        | ...     | ...               | ...                  | ...      |     ...        | ...          |  ...                                 | ...       | ...       | ...     | ...         |   ...      | ...             |   ...    | ...        | ...       |  ...      | ...              | ...              | ...            | ...            | ...            |

* Save data to CSV:

```python
import statsbomb as sb

events = sb.Events(event_id='8658')
events.save_data(event_type='shot')  # outputs a file named events_8658_shot.csv
```
