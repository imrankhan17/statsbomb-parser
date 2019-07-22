from httmock import all_requests, HTTMock, response
import json
import os
import statsbomb as sb


def test_parser():

    @all_requests
    def github_mock(url, request):
        content = json.load(open(os.path.join(os.path.dirname(__file__), 'test_data', '49', '3.json'),
                                 encoding='utf-8'))
        return response(content=content, request=request)

    with HTTMock(github_mock):
        matches = sb.Matches(event_id='49', season_id='3')

    assert str(matches) == 'Matches data for ID: 49_3'
    assert matches.id == '49_3'
    assert len(matches) == 12
    assert matches.get_dataframe().to_dict(orient='records') == [
        {'away_score': 1, 'away_team': 761, 'competition': 49, 'data_version': '1.0.2', 'home_score': 1,
         'home_team': 766, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-05-06',
         'match_id': 7444, 'match_status': 'available', 'referee_name': 'M. Vega', 'season': 3,
         'stadium_name': "Sahlen's Stadium at WakeMed Soccer Park"},
        {'away_score': 4, 'away_team': 766, 'competition': 49, 'data_version': '1.0.2', 'home_score': 1,
         'home_team': 765, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-05-31',
         'match_id': 7519, 'match_status': 'available', 'referee_name': 'Joe Dickerson', 'season': 3,
         'stadium_name': 'Providence Park'},
        {'away_score': 2, 'away_team': 766, 'competition': 49, 'data_version': '1.0.2', 'home_score': 1,
         'home_team': 763, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-05-20',
         'match_id': 7456, 'match_status': 'available', 'referee_name': 'D. Chesky', 'season': 3,
         'stadium_name': 'Yurcak Field'},
        {'away_score': 4, 'away_team': 766, 'competition': 49, 'data_version': '1.0.2', 'home_score': 3,
         'home_team': 764, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-05-24',
         'match_id': 7457, 'match_status': 'available', 'referee_name': 'C. Unkel', 'season': 3,
         'stadium_name': 'Orlando City Stadium'},
        {'away_score': 0, 'away_team': 759, 'competition': 49, 'data_version': '1.0.2', 'home_score': 2,
         'home_team': 766, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-12',
         'match_id': 7482, 'match_status': 'available', 'referee_name': 'D. Gutierrez', 'season': 3,
         'stadium_name': "Sahlen's Stadium at WakeMed Soccer Park"},
        {'away_score': 0, 'away_team': 766, 'competition': 49, 'data_version': '1.0.2', 'home_score': 0,
         'home_team': 767, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-21',
         'match_id': 7487, 'match_status': 'available', 'referee_name': 'C. Unkel', 'season': 3,
         'stadium_name': 'Rio Tinto Stadium'},
        {'away_score': 2, 'away_team': 764, 'competition': 49, 'data_version': '1.0.2', 'home_score': 1,
         'home_team': 767, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-14',
         'match_id': 7483, 'match_status': 'available', 'referee_name': 'R. Fonseca', 'season': 3,
         'stadium_name': 'Rio Tinto Stadium'},
        {'away_score': 1, 'away_team': 762, 'competition': 49, 'data_version': '1.0.2', 'home_score': 3,
         'home_team': 765, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-16',
         'match_id': 7486, 'match_status': 'available', 'referee_name': 'E. Tattersall', 'season': 3,
         'stadium_name': 'Providence Park'},
        {'away_score': 4, 'away_team': 766, 'competition': 49, 'data_version': '1.0.2', 'home_score': 0,
         'home_team': 763, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-15',
         'match_id': 7484, 'match_status': 'available', 'referee_name': 'D. Chesky', 'season': 3,
         'stadium_name': 'Yurcak Field'},
        {'away_score': 1, 'away_team': 763, 'competition': 49, 'data_version': '1.0.2', 'home_score': 3,
         'home_team': 767, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-01',
         'match_id': 7473, 'match_status': 'available', 'referee_name': 'V. Rivas', 'season': 3,
         'stadium_name': 'Rio Tinto Stadium'},
        {'away_score': 1, 'away_team': 759, 'competition': 49, 'data_version': '1.0.2', 'home_score': 2,
         'home_team': 764, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-08',
         'match_id': 7479, 'match_status': 'available', 'referee_name': 'D. Chesky', 'season': 3,
         'stadium_name': 'Orlando City Stadium'},
        {'away_score': 0, 'away_team': 760, 'competition': 49, 'data_version': '1.0.2', 'home_score': 1,
         'home_team': 761, 'kick_off': None, 'last_updated': '2018-09-08T07:33:39.356340', 'match_date': '2018-07-15',
         'match_id': 7485, 'match_status': 'available', 'referee_name': 'N. Simon', 'season': 3,
         'stadium_name': 'Toyota Park'}
    ]
