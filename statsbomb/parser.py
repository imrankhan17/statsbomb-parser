import json
import pandas as pd

from statsbomb.utils import columns, get_event_name


class Events:
    """

    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = json.load(open(self.file_path))
        self.match_id = self.file_path.split('/')[-1].split('.json')[0]

    def __repr__(self):
        return 'Events for match ID {}'.format(self.match_id)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.data)

    def get_dataframe(self, event_type: str) -> pd.DataFrame:

        assert event_type.title() in columns['events'], '`{}` is not a valid event type'.format(event_type)

        all_events = [i for i in self.data if i['type']['name'] == event_type.title()]
        assert len(all_events) > 0, 'Found 0 events for `{}`'.format(event_type)

        common_elements = [{key: event.get(key, None) for key in columns['common']} for event in all_events]

        event_objects = []
        for event in all_events:
            object_dict = {}
            for key in columns[event_type]:
                try:
                    object_dict[key] = event[event_type.replace(' ', '_')].get(key, None)
                except KeyError:
                    object_dict[key] = None
            event_objects.append(object_dict)

        final = [{**i, **j} for i, j in zip(common_elements, event_objects)]

        df = pd.DataFrame(final)

        for col in columns['name_cols']:
            try:
                df[col] = df[col].apply(get_event_name)
            except KeyError:
                pass

        try:
            df[['start_location_x', 'start_location_y']] = df['location'].apply(pd.Series)
        except ValueError:
            pass
        df = df.drop('location', axis=1)

        if 'end_location' in df.columns:
            try:
                df[['end_location_x', 'end_location_y', 'end_location_z']] = df['end_location'].apply(pd.Series)
            except ValueError:
                df[['end_location_x', 'end_location_y']] = df['end_location'].apply(pd.Series)
            df = df.drop('end_location', axis=1)

        return df
