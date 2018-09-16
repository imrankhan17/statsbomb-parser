import os
import statsbomb as sb


def test_parser():
    comps = sb.Competitions(os.path.join(os.path.dirname(__file__), 'test_data', 'competitions.json'))

    assert str(comps) == 'Competitions data for ID: competitions'
    assert comps.id == 'competitions'
    assert len(comps) == 3
    assert comps.get_dataframe().to_dict(orient='records') == [
        {'competition_id': 37, 'competition_name': "FA Women's Super League", 'country_name': 'England',
         'match_available': '2018-09-08T07:33:39.356340', 'match_updated': '2018-09-08T07:33:39.356340',
         'season_id': 1, 'season_name': '2017/2018'},
        {'competition_id': 43, 'competition_name': 'FIFA World Cup', 'country_name': 'International',
         'match_available': '2018-09-08T07:33:39.356340', 'match_updated': '2018-09-08T14:30:04.356514',
         'season_id': 3, 'season_name': '2018'},
        {'competition_id': 49, 'competition_name': 'NWSL', 'country_name': 'United States of America',
         'match_available': '2018-09-08T07:33:39.356340', 'match_updated': '2018-09-08T07:33:39.356340',
         'season_id': 3, 'season_name': '2018'}
    ]
