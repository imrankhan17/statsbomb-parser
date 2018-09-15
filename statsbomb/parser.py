import json
import pandas as pd

from statsbomb.utils import columns, get_event_name


class Events:
    """

    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = json.load(open(self.file_path))

    def get_shots(self):
        all_shots = [i for i in self.data if 'shot' in i.keys()]
        shots = [{key: shot.get(key, None) for key in columns['common'] + columns['shot']} for shot in all_shots]
        shot_objects = [{key: shot['shot'].get(key, None) for key in columns['shot_objects']} for shot in all_shots]
        final = [{**i, **j} for i, j in zip(shots, shot_objects)]

        df = pd.DataFrame(final)

        for col in columns['name_cols']:
            df[col] = df[col].apply(get_event_name)

        df[['start_location_x', 'start_location_y']] = df['location'].apply(pd.Series)
        df[['end_location_x', 'end_location_y', 'end_location_z']] = df['end_location'].apply(pd.Series)
        df = df.drop(['location', 'end_location'], axis=1)

        return df
