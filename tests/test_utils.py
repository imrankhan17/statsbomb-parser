from statsbomb.utils import get_event_name


def test_get_event_name():
    assert get_event_name({'name': 'value'}) == 'value'
    assert get_event_name({'name': 1}) == 1
    assert get_event_name({'name': 'value', 'other_key': 'value2'}) == 'value'
    assert get_event_name({'other': 'value'}) is None
    assert get_event_name({}) is None
