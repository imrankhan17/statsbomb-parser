import pytest
import statsbomb as sb


def test_base():

    with pytest.raises(Exception):
        base_class = sb.parser.BaseParser(event_id='9999')  # pylint: disable=unused-variable
