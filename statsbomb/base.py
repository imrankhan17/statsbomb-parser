from json import JSONDecodeError
import os
import pandas as pd
import requests

from statsbomb.utils import BASE_URL


class BaseParser:
    """
    Base class for parsers.
    """
    def __init__(self, event_id: str = None):
        self.id = event_id
        try:
            self.data = requests.get(self._construct_url()).json()
        except JSONDecodeError:
            raise Exception('No data found for {} ID: {}'.format(self.__class__.__name__.lower(), self.id))

    def __repr__(self):
        return '{} data for ID: {}'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.data)

    def _construct_url(self):
        return '{}/{}/{}.json'.format(BASE_URL, self.__class__.__name__.lower(), self.id)

    def get_dataframe(self, **kwargs) -> pd.DataFrame:
        raise NotImplementedError

    def save_data(self, event_type: str = None, tmp: bool = False, **kwargs):

        df = self.get_dataframe(event_type=event_type)

        if event_type:
            file_name = '{}_{}_{}.csv'.format(self.__class__.__name__.lower(), self.id, event_type)
        else:
            file_name = '{}_{}.csv'.format(self.__class__.__name__.lower(), self.id)

        if tmp:
            file_path = os.path.join('tmp', file_name)
        else:
            file_path = file_name

        df.to_csv(file_path, index=False)
