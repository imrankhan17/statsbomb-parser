import os
import yaml


BASE_URL = 'https://raw.githubusercontent.com/statsbomb/open-data/master/data'

columns = yaml.load(open(os.path.join(os.path.dirname(__file__), 'events.yaml')))


def get_event_name(dictionary: dict):
    """Gets value from dictionary for key `name` other returns None"""
    try:
        return dictionary.get('name', None)
    except AttributeError:
        return None
