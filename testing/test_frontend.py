import pytest
from  frontend.Frontend import Data_processing 

@pytest.fixture
def data_processing():
    "creates a fresh instance of the class before every time"
    return Data_processing()

def test_get_column_types():
    assert Data_processing.get_column_types() == {flight: str}

def test_check_data():
    assert Data_processing.check_data(df) == df
