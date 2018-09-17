import os
import pytest
import statsbomb as sb


def test_base():
    base_class = sb.parser.BaseParser(os.path.join(os.path.dirname(__file__), 'test_data', 'competitions.json'))

    assert str(base_class) == 'BaseParser data for ID: competitions'
    assert base_class.id == 'competitions'
    assert len(base_class) == 3

    with pytest.raises(NotImplementedError):
        base_class.get_dataframe()
