import pytest
from src.readers.file_reader import read_definition


class TestRead:
    def test_read_definition(self):
        content = read_definition("src/definitions/http-definition.yaml")
        assert content
        assert content is not None
        assert "protocol" in content
