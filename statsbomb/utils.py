import yaml


columns = yaml.load(open('headers.yaml'))


def get_event_name(x):
    return x['name']

