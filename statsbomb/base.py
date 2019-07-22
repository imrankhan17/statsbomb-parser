from json import JSONDecodeError
import os
import pandas as pd
import requests

from statsbomb.utils import BASE_URL


class BaseParser:
    """
    Base class for parsers.
    """
    def __init__(self, event_id: str = None, season_id: str = None):
        self.event_id = event_id
        self.season_id = season_id
        self.id = self._construct_id
        try:
            self.data = requests.get(self._construct_url()).json()
        except JSONDecodeError:
            raise Exception(f'No data found for {self.__class__.__name__.lower()} ID: {self.id}, '
                            f'URL: {self._construct_url()}')

    def __repr__(self):
        return f'{self.__class__.__name__} data for ID: {self.id}'

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.data)

    @property
    def _construct_id(self):
        if None not in (self.event_id, self.season_id):
            return f'{self.event_id}_{self.season_id}'

        if self.season_id is None:
            return self.event_id

        return self.season_id

    def _construct_url(self):
        return f"{BASE_URL}/{self.__class__.__name__.lower()}/{self.id.replace('_', '/')}.json"

    def get_dataframe(self, **kwargs) -> pd.DataFrame:
        raise NotImplementedError

    def save_data(self, event_type: str = None, tmp: bool = False):

        df = self.get_dataframe(event_type=event_type)

        if event_type:
            file_name = f'{self.__class__.__name__.lower()}_{self.id}_{event_type}.csv'
        else:
            file_name = f'{self.__class__.__name__.lower()}_{self.id}.csv'

        if tmp:
            file_path = os.path.join(os.sep, 'tmp', file_name)
        else:
            file_path = file_name

        df.to_csv(file_path, index=False)
