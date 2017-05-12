import pytest
import json

from flex.exceptions import DataCouldNotBeParsed

from tests.factories import (
    ResponseFactory,
)


def test_invalid_json():
    body = '{"trailing comma not valid": [1,]}'
    request = ResponseFactory(
        content=body,
        content_type='application/json',
    )
    with pytest.raises(DataCouldNotBeParsed):
        request.data