from httmock import all_requests, HTTMock, response
import json
import os
import statsbomb as sb


def test_parser():

    @all_requests
    def github_mock(url, request):
        content = json.load(open(os.path.join(os.path.dirname(__file__), 'test_data', '7457.json'), encoding='utf-8'))
        return response(content=content, request=request)

    with HTTMock(github_mock):
        lineup = sb.Lineups(event_id='7457')

    assert str(lineup) == 'Lineups data for ID: 7457'
    assert lineup.id == '7457'
    assert len(lineup) == 2
    assert lineup.get_dataframe().to_dict(orient='records') == [
        {'country': 'United States of America', 'jersey_number': 14, 'player_id': 5034,
         'player_name': 'Jessica McDonald', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'New Zealand', 'jersey_number': 6, 'player_id': 5037, 'player_name': 'Abby Erceg', 'team_id': 766,
         'team_name': 'North Carolina Courage'},
        {'country': 'Brazil', 'jersey_number': 10, 'player_id': 5044,
         'player_name': 'Debora Cristiane de Oliveira', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 15, 'player_id': 5047,
         'player_name': 'Jaelene Hinkle', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 0, 'player_id': 5048,
         'player_name': 'Katelyn Rowland', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 25, 'player_id': 5050,
         'player_name': 'Meredith Speck', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 23, 'player_id': 5080,
         'player_name': 'Kristen Hamilton', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 13, 'player_id': 5081,
         'player_name': 'Abby Dahlkemper', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 11, 'player_id': 5083,
         'player_name': 'Merritt Mathias', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'Ireland', 'jersey_number': 8, 'player_id': 5084, 'player_name': "Denise O'Sullivan",
         'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 5, 'player_id': 5087, 'player_name': 'Samantha Mewis',
         'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 19, 'player_id': 5088,
         'player_name': 'Crystal Alyssia Dunn', 'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'United States of America', 'jersey_number': 7, 'player_id': 5091, 'player_name': 'McCall Zerboni',
         'team_id': 766, 'team_name': 'North Carolina Courage'},
        {'country': 'Brazil', 'jersey_number': 19, 'player_id': 5060, 'player_name': 'Poliana Barbosa Medeiros',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 17, 'player_id': 5062,
         'player_name': 'Dani Weatherholt', 'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 6, 'player_id': 5063, 'player_name': 'Chioma Ubogagu',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 16, 'player_id': 5064,
         'player_name': 'Carson Pickett', 'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 12, 'player_id': 5068,
         'player_name': 'Kristen Edmonds', 'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 7, 'player_id': 5070,
         'player_name': 'Christine Nairn', 'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'Canada', 'jersey_number': 4, 'player_id': 5074, 'player_name': 'Shelina Zadorsky', 'team_id': 764,
         'team_name': 'Orlando Pride'},
        {'country': 'Australia', 'jersey_number': 5, 'player_id': 5076, 'player_name': 'Emily van Egmond',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'Australia', 'jersey_number': 14, 'player_id': 5078, 'player_name': 'Alanna Kennedy',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'Brazil', 'jersey_number': 10, 'player_id': 5082, 'player_name': 'Marta Vieira da Silva',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 13, 'player_id': 5085, 'player_name': 'Alex Morgan',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 15, 'player_id': 5086, 'player_name': 'Rachel Hill',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 11, 'player_id': 5089, 'player_name': 'Ali Krieger',
         'team_id': 764, 'team_name': 'Orlando Pride'},
        {'country': 'United States of America', 'jersey_number': 24, 'player_id': 5090, 'player_name': 'Ashlyn Harris',
         'team_id': 764, 'team_name': 'Orlando Pride'}
    ]
