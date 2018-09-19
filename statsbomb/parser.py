import pandas as pd

from statsbomb.base import BaseParser
from statsbomb.utils import BASE_URL, columns, get_event_name


class Competitions(BaseParser):
    """
    Parses 'data/competitions.json' into tabular format.
    """

    def _construct_url(self):
        return '{}/{}.json'.format(BASE_URL, self.__class__.__name__.lower())

    def get_dataframe(self, **kwargs) -> pd.DataFrame:
        return pd.DataFrame(self.data)


class Matches(BaseParser):
    """
    Parses json data stored under 'data/matches/' into tabular format.
    """
    def get_dataframe(self, **kwargs) -> pd.DataFrame:

        df = pd.DataFrame(self.data)
        for col in columns['matches_name_cols']:
            df[col] = df[col].apply(pd.Series)

        return df


class Lineups(BaseParser):
    """
    Parses json data stored under 'data/lineups/' into tabular format.
    """
    def get_dataframe(self, **kwargs) -> pd.DataFrame:

        df = pd.DataFrame()
        for team in self.data:
            lineup = pd.DataFrame(team['lineup'])
            lineup['team_id'] = team['team_id']
            lineup['team_name'] = team['team_name']
            df = df.append(lineup).reset_index(drop=True)

        df['country'] = df['country'].apply(get_event_name)

        return df


class Events(BaseParser):
    """
    Parses json data stored under 'data/events/' into tabular format for a particular event.
    """

    def get_dataframe(self, event_type: str) -> pd.DataFrame:

        assert event_type.title() in columns['events'], '`{}` is not a valid event type'.format(event_type)

        # get all events for a given event type
        all_events = [i for i in self.data if i['type']['name'] == event_type.title()]
        assert all_events, 'Found 0 events for `{}`'.format(event_type)

        # get common attributes
        common_elements = [{key: event.get(key, None) for key in columns['common']} for event in all_events]

        # get attributes specific to this event type
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

        # combine all into one dataframe and order columns
        df = pd.DataFrame(final)
        df['event_type'] = event_type
        df = df[['event_type'] + columns['common'] + columns[event_type]]

        # get names from attributes of form: `{"id" : 7, "name" : "From Goal Kick"}`
        name_cols = [i for i in df.columns if i in columns['name_cols']]
        df[name_cols] = df[name_cols].applymap(get_event_name)

        # split location arrays into their own columns
        try:
            df[['start_location_x', 'start_location_y']] = df['location'].apply(pd.Series)
        except ValueError:
            pass
        df = df.drop('location', axis=1)

        # only the shot event type has a z coordinate
        if 'end_location' in df.columns:
            try:
                df[['end_location_x', 'end_location_y', 'end_location_z']] = df['end_location'].apply(pd.Series)
            except ValueError:
                df[['end_location_x', 'end_location_y']] = df['end_location'].apply(pd.Series)
            df = df.drop('end_location', axis=1)

        return df
