"""
    Deutscher Wetterdienst: API

    Aktuelle Wetterdaten von allen Deutschen Wetterstationen  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dwd.model.station_overview10865_days import StationOverview10865Days
from deutschland.dwd.model.station_overview10865_forecast1 import (
    StationOverview10865Forecast1,
)
from deutschland.dwd.model.station_overview10865_forecast2 import (
    StationOverview10865Forecast2,
)

from deutschland import dwd

globals()["StationOverview10865Days"] = StationOverview10865Days
globals()["StationOverview10865Forecast1"] = StationOverview10865Forecast1
globals()["StationOverview10865Forecast2"] = StationOverview10865Forecast2
from deutschland.dwd.model.station_overview10865 import StationOverview10865


class TestStationOverview10865(unittest.TestCase):
    """StationOverview10865 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStationOverview10865(self):
        """Test StationOverview10865"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StationOverview10865()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
