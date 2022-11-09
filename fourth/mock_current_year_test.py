import unittest
import io
from unittest.mock import patch
import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    def test_YMD(self):
        data = io.StringIO('{"currentDateTime": "1923-09-11"}')
        with patch.object(what_is_year_now.urllib.request, 'urlopen', return_value=data):
            assert what_is_year_now.get_current_year() == 1923

    def test_DMY(self):
        data = io.StringIO('{"currentDateTime": "20.43.1052"}')
        with patch.object(what_is_year_now.urllib.request, 'urlopen', return_value=data):
            assert what_is_year_now.get_current_year() == 1052

    def test_invalid_format(self):
        data = io.StringIO('{"currentDateTime": "1th September 2022"}')
        with self.assertRaises(ValueError):
            with patch.object(what_is_year_now.urllib.request, 'urlopen', return_value=data):
                assert what_is_year_now.get_current_year()

