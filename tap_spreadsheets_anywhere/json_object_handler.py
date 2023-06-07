import json
from typing import TextIO, Iterator, Any


def get_row_iterator(table_spec, reader: TextIO) -> Iterator[Any]:
    yield json.load(reader)
