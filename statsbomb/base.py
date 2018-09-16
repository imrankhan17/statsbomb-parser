import json


class BaseParser:
    """
    Base class for parsers.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = json.load(open(self.file_path, encoding='utf-8'))
        self.id = self.file_path.split('/')[-1].split('.json')[0]

    def __repr__(self):
        return '{} data for ID: {}'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.data)
