from main import light_times_valid
import pytest

class TestClass:

    # @pytest.fixture(scope='function')
    # def prius(self):                                                      
    #     return Car("Prius", "2004", "white")

    def test_valid_time(self):
        assert light_times_valid(1, 2, 3) == True

    def test_invalid_time(self):
        assert light_times_valid(10, 12, 13) == False