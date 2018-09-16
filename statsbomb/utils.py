import os
import yaml


columns = yaml.load(open(os.path.join(os.path.dirname(__file__), 'events.yaml')))


def get_event_name(x):
    try:
        return x.get('name', None)
    except AttributeError:
        return None
