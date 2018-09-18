from httmock import all_requests, HTTMock, response
import json
import os
import pytest
import statsbomb as sb


@pytest.fixture(scope='module')
def events_json():

    @all_requests
    def github_mock(url, request):
        content = json.load(open(os.path.join(os.path.dirname(__file__), 'test_data', '8656.json'), encoding='utf-8'))
        return response(content=content, request=request)

    with HTTMock(github_mock):
        events = sb.Events(event_id='8656')

    return events


def test_class():
    events = events_json()
    assert str(events) == 'Events data for ID: 8656'
    assert events.id == '8656'
    assert len(events) == 16

    with pytest.raises(AssertionError):
        events.get_dataframe('fake_event')

    with pytest.raises(AssertionError):
        events.get_dataframe('block')


def test_shots():
    events = events_json()
    assert events.get_dataframe('shot').to_dict(orient='records') == [
        {'event_type': 'shot', 'id': '0160a53e-9ed5-48ff-adfe-be306d551b4a', 'index': 95, 'period': 1,
         'timestamp': '00:04:46.900', 'minute': 4, 'second': 46, 'possession': 10, 'possession_team': 'England',
         'play_pattern': 'From Free Kick', 'off_camera': False, 'team': 'England', 'player': 'Kieran Trippier',
         'position': 'Right Wing Back', 'duration': 1.013, 'under_pressure': None, 'statsbomb_xg': 0.08887702,
         'key_pass_id': None, 'body_part': 'Right Foot', 'type': 'Free Kick', 'outcome': 'Goal', 'technique': 'Normal',
         'first_time': None, 'follows_dribble': None, 'redirect': None, 'one_on_one': None, 'open_goal': None,
         'deflected': None, 'start_location_x': 96.0, 'start_location_y': 43.0, 'end_location_x': 120.0,
         'end_location_y': 43.1, 'end_location_z': 2.1},
        {'event_type': 'shot', 'id': '48e28801-8408-4b74-806a-5f1e40224cce', 'index': 307, 'period': 1,
         'timestamp': '00:13:41.780', 'minute': 13, 'second': 41, 'possession': 27, 'possession_team': 'England',
         'play_pattern': 'From Corner', 'off_camera': False, 'team': 'England', 'player': 'Harry Maguire',
         'position': 'Left Center Back', 'duration': 1.453, 'under_pressure': None, 'statsbomb_xg': 0.013174075,
         'key_pass_id': 'd492f17b-6dd5-45d1-aa51-ce32436a57a3', 'body_part': 'Head', 'type': 'Open Play',
         'outcome': 'Off T', 'technique': 'Normal', 'first_time': None, 'follows_dribble': None, 'redirect': None,
         'one_on_one': None, 'open_goal': None, 'deflected': None, 'start_location_x': 111.0, 'start_location_y': 37.0,
         'end_location_x': 120.0, 'end_location_y': 45.1, 'end_location_z': 0.3},
        {'event_type': 'shot', 'id': 'f25a693f-81cd-41ec-a57f-957da6eb7626', 'index': 436, 'period': 1,
         'timestamp': '00:18:18.313', 'minute': 18, 'second': 18, 'possession': 37, 'possession_team': 'Croatia',
         'play_pattern': 'From Throw In', 'off_camera': False, 'team': 'Croatia', 'player': 'Ivan Perisic',
         'position': 'Left Wing', 'duration': 1.067, 'under_pressure': None, 'statsbomb_xg': 0.03211567,
         'key_pass_id': 'f695d356-f55d-4eb5-9069-8a8e157eef53', 'body_part': 'Right Foot', 'type': 'Open Play',
         'outcome': 'Off T', 'technique': 'Normal', 'first_time': None, 'follows_dribble': None, 'redirect': None,
         'one_on_one': None, 'open_goal': None, 'deflected': True, 'start_location_x': 94.0, 'start_location_y': 20.0,
         'end_location_x': 120.0, 'end_location_y': 34.9, 'end_location_z': 0.5}
    ]


def test_passes():
    events = events_json()
    assert events.get_dataframe('pass').to_dict(orient='records') == [
        {'event_type': 'pass', 'id': '7e92f6b8-48e8-4616-9997-de689e48e4fd', 'index': 439, 'period': 1,
         'timestamp': '00:18:59.780', 'minute': 18, 'second': 59, 'possession': 38, 'possession_team': 'England',
         'play_pattern': 'From Throw In', 'off_camera': False, 'team': 'England', 'player': 'Ashley Young',
         'position': 'Left Wing Back', 'duration': 3.56, 'under_pressure': None, 'recipient': 'Harry Maguire',
         'length': 38.078865, 'angle': 2.7367008, 'height': 'High Pass', 'outcome': None, 'type': 'Throw-in',
         'body_part': None, 'assisted_shot_id': None, 'pass_backheel': None, 'deflected': None,
         'miscommunication': None, 'through_ball': None, 'cross': None, 'cut_back': None, 'switch': None,
         'shot_assist': None, 'goal_assist': None, 'start_location_x': 55.0, 'start_location_y': 1.0,
         'end_location_x': 20.0, 'end_location_y': 16.0},
        {'event_type': 'pass', 'id': '0a7f0193-8257-40f3-b19b-2b046c5a08bc', 'index': 450, 'period': 1,
         'timestamp': '00:19:11.860', 'minute': 19, 'second': 11, 'possession': 38, 'possession_team': 'England',
         'play_pattern': 'From Throw In', 'off_camera': False, 'team': 'England', 'player': 'Kieran Trippier',
         'position': 'Right Wing Back', 'duration': 3.973, 'under_pressure': None, 'recipient': 'Raheem Sterling',
         'length': 32.38827, 'angle': -0.15499674, 'height': 'High Pass', 'outcome': 'Incomplete', 'type': None,
         'body_part': 'Left Foot', 'assisted_shot_id': None, 'pass_backheel': None, 'deflected': None,
         'miscommunication': None, 'through_ball': None, 'cross': None, 'cut_back': None, 'switch': None,
         'shot_assist': None, 'goal_assist': None, 'start_location_x': 74.0, 'start_location_y': 78.0,
         'end_location_x': 106.0, 'end_location_y': 73.0},
        {'event_type': 'pass', 'id': '510783ec-ea0e-4674-8e78-82e2147507a2', 'index': 3057, 'period': 4,
         'timestamp': '00:03:01.550', 'minute': 108, 'second': 1, 'possession': 229, 'possession_team': 'Croatia',
         'play_pattern': 'From Throw In', 'off_camera': False, 'team': 'Croatia', 'player': 'Ivan Perisic',
         'position': 'Left Wing', 'duration': 2.08, 'under_pressure': None, 'recipient': 'Mario Mandzukic',
         'length': 15.556349, 'angle': 0.7853982, 'height': 'High Pass', 'outcome': None, 'type': 'Recovery',
         'body_part': 'Head', 'assisted_shot_id': '5a2e748a-46e8-4f7e-936a-1beae50b693d', 'pass_backheel': None,
         'deflected': None, 'miscommunication': None, 'through_ball': None, 'cross': None, 'cut_back': None,
         'switch': None, 'shot_assist': None, 'goal_assist': True, 'start_location_x': 103.0, 'start_location_y': 20.0,
         'end_location_x': 114.0, 'end_location_y': 31.0},
        {'event_type': 'pass', 'id': '7cfa57b4-9003-462a-b11a-5979f95639ac', 'index': 3170, 'period': 4,
         'timestamp': '00:10:59.150', 'minute': 115, 'second': 59, 'possession': 239, 'possession_team': 'England',
         'play_pattern': 'From Free Kick', 'off_camera': False, 'team': 'England', 'player': 'Jordan Pickford',
         'position': 'Goalkeeper', 'duration': 3.48, 'under_pressure': None, 'recipient': 'Harry Kane',
         'length': 71.063354, 'angle': -0.0422284, 'height': 'High Pass', 'outcome': 'Incomplete', 'type': 'Free Kick',
         'body_part': 'Left Foot', 'assisted_shot_id': None, 'pass_backheel': None, 'deflected': None,
         'miscommunication': None, 'through_ball': None, 'cross': None, 'cut_back': None, 'switch': None,
         'shot_assist': None, 'goal_assist': None, 'start_location_x': 14.0, 'start_location_y': 38.0,
         'end_location_x': 85.0, 'end_location_y': 35.0}
    ]


def test_ball_recovery():
    events = events_json()
    assert events.get_dataframe('ball recovery').to_dict(orient='records') == [
        {'event_type': 'ball recovery', 'id': '89300a03-5ea3-4962-96d2-ba8d613f0dae', 'index': 3208, 'period': 4,
         'timestamp': '00:13:42.563', 'minute': 118, 'second': 42, 'possession': 242, 'possession_team': 'England',
         'play_pattern': 'From Counter', 'off_camera': False, 'team': 'England', 'player': 'Harry Maguire',
         'position': 'Left Center Back', 'duration': None, 'under_pressure': None, 'offensive': None,
         'recovery_failure': None, 'start_location_x': 51.0, 'start_location_y': 8.0}
    ]


def test_ball_receipt():
    events = events_json()
    assert events.get_dataframe('ball receipt*').to_dict(orient='records') == [
        {'event_type': 'ball receipt*', 'id': 'd12476d5-363d-4779-89d7-22fe06c60610', 'index': 3211, 'period': 4,
         'timestamp': '00:13:46.563', 'minute': 118, 'second': 46, 'possession': 242, 'possession_team': 'England',
         'play_pattern': 'From Counter', 'off_camera': False, 'team': 'England', 'player': 'John Stones',
         'position': 'Right Center Back', 'duration': None, 'under_pressure': True, 'outcome': None,
         'start_location_x': 51.0, 'start_location_y': 25.0},
        {'event_type': 'ball receipt*', 'id': '3fe3b28b-70a3-4859-a4a8-a34afdc305a8', 'index': 3218, 'period': 4,
         'timestamp': '00:13:57.430', 'minute': 118, 'second': 57, 'possession': 242, 'possession_team': 'England',
         'play_pattern': 'From Counter', 'off_camera': False, 'team': 'England', 'player': 'Jamie Vardy',
         'position': 'Left Center Forward', 'duration': None, 'under_pressure': None, 'outcome': None,
         'start_location_x': 96.0, 'start_location_y': 60.0}
    ]


def test_substitution():
    events = events_json()
    assert events.get_dataframe('substitution').to_dict(orient='records') == [
        {'event_type': 'substitution', 'id': '59dfc811-3891-4316-a299-59cafe91a99d', 'index': 1949, 'period': 2,
         'timestamp': '00:28:10.693', 'minute': 73, 'second': 10, 'possession': 151, 'possession_team': 'Croatia',
         'play_pattern': 'From Corner', 'off_camera': False, 'team': 'England', 'player': 'Raheem Sterling',
         'position': 'Left Center Forward', 'duration': None, 'under_pressure': None,
         'replacement': {'id': 3318, 'name': 'Marcus Rashford'}, 'outcome': 'Tactical'}
    ]
