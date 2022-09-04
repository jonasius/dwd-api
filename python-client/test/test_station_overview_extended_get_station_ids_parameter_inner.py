"""
    Deutscher Wetterdienst: API

    API des Deutschen Wetterdienstes (DWD) aus der DWD App. <br><br> Neben unterschiedlichen Wetterwarnungen (s.u.) lassen sich unter [/dwd.api.proxy.bund.dev/v30/stationOverviewExtended](/dwd.api.proxy.bund.dev/v30/stationOverviewExtended) nach Angabe des Parameters *stationIDs* (z.B. 'G005') auch die Wetterdaten ausgewählter Wetterstationen anfordern (wobei die sog. 'Stationskennung' des DWD anzugeben ist). <br><br> Unter [https://opendata.dwd.de/](https://opendata.dwd.de/) bietet der DWD darüber hinaus auch aktuelle und historische Daten zu diversen Wetterdaten zum Download an (vgl. hierzu die offizielle Dokumentation [hier](https://opendata.dwd.de/climate_environment/CDC/Readme_intro_CDC_ftp.pdf)). In diesem Zusammenhang erwähnenswert ist auch eine weitere offizielle Liste aller Wetterstationen (ohne Stationskennung aber mit sog. 'Stations_id') [hier](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/KL_Tageswerte_Beschreibung_Stationen.txt).  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dwd.model.station_overview_extended_get_station_ids_parameter_inner import (
    StationOverviewExtendedGetStationIdsParameterInner,
)

from deutschland import dwd


class TestStationOverviewExtendedGetStationIdsParameterInner(unittest.TestCase):
    """StationOverviewExtendedGetStationIdsParameterInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStationOverviewExtendedGetStationIdsParameterInner(self):
        """Test StationOverviewExtendedGetStationIdsParameterInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StationOverviewExtendedGetStationIdsParameterInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
