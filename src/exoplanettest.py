
from exoplanet import ExoPlanet
import unittest
from collections import Counter

DATASET = [

    {
        "PlanetIdentifier": "Kepler-1289 b",
        "TypeFlag": 3,
        "PlanetaryMassJpt": "",
        "RadiusJpt": 0.136,
        "PeriodDays": 7.99019627,
        "SemiMajorAxisAU": "",
        "Eccentricity": "",
        "PeriastronDeg": "",
        "LongitudeDeg": "",
        "AscendingNodeDeg": "",
        "InclinationDeg": "",
        "SurfaceTempK": "",
        "AgeGyr": "",
        "DiscoveryMethod": "transit",
        "DiscoveryYear": 2016,
        "LastUpdated": "16/05/10",
        "RightAscension": "19 45 33",
        "Declination": "+41 02 26",
        "DistFromSunParsec": "",
        "HostStarMassSlrMass": 1.1,
        "HostStarRadiusSlrRad": 1.17,
        "HostStarMetallicity": 0.02,
        "HostStarTempK": 6080,
        "HostStarAgeGyr": ""
    },
    {
        "PlanetIdentifier": "OGLE-TR-10 b",
        "TypeFlag": 0,
        "PlanetaryMassJpt": 0.68,
        "RadiusJpt": 1.72,
        "PeriodDays": 3.10129,
        "SemiMajorAxisAU": 0.04516,
        "Eccentricity": 0,
        "PeriastronDeg": "",
        "LongitudeDeg": "",
        "AscendingNodeDeg": "",
        "InclinationDeg": 84.5,
        "SurfaceTempK": 1702,
        "AgeGyr": "",
        "DiscoveryMethod": "transit",
        "DiscoveryYear": 2004,
        "LastUpdated": "10/06/24",
        "RightAscension": "17 51 28",
        "Declination": "-29 52 34",
        "DistFromSunParsec": 1500,
        "HostStarMassSlrMass": 1.277,
        "HostStarRadiusSlrRad": 1.52,
        "HostStarMetallicity": 0.28,
        "HostStarTempK": 6075,
        "HostStarAgeGyr": ""
    },
    {
        "PlanetIdentifier": "Gliese 1214 b",
        "TypeFlag": 3,
        "PlanetaryMassJpt": 0.0195,
        "RadiusJpt": 0.2525,
        "PeriodDays": 1.58040417,
        "SemiMajorAxisAU": 0.01488,
        "Eccentricity": 0,
        "PeriastronDeg": "",
        "LongitudeDeg": "",
        "AscendingNodeDeg": "",
        "InclinationDeg": 88.47,
        "SurfaceTempK": 604,
        "AgeGyr": "",
        "DiscoveryMethod": "transit",
        "DiscoveryYear": 2009,
        "LastUpdated": "10/12/07",
        "RightAscension": "17 15 18.94",
        "Declination": "+04 57 49.7",
        "DistFromSunParsec": 14.55,
        "HostStarMassSlrMass": 0.176,
        "HostStarRadiusSlrRad": 0.2213,
        "HostStarMetallicity": 0.1,
        "HostStarTempK": 3250,
        "HostStarAgeGyr": ""
    },
]


class TestExoPlanet(unittest.TestCase):

    def setUp(self):

        self.ep = ExoPlanet()

    def test_get_hottest_star(self):

        self.ep.dataset_ = DATASET
        hottest_planet = self.ep.get_planet_orbiting_hottest_star()
        self.assertEqual(hottest_planet['PlanetIdentifier'], 'Kepler-1289 b')

    def test_get_list_of_orphan_planet_name(self):

        self.ep.dataset_ = DATASET
        self.assertEqual(self.ep.get_list_of_orphan_planet_name(), ['Kepler-1289 b', 'Gliese 1214 b'])

    def test_get_planet_timeline(self):

        self.ep.dataset_ = DATASET
        self.assertEqual(self.ep.get_planet_timeline(), {2004: Counter({'medium': 1, 'small': 0, 'large': 0}),
                                    2009: Counter({'small': 1, 'medium': 0, 'large': 0}),
                                    2016: Counter({'small': 1, 'medium': 0, 'large': 0})})

    def test_get_planet_orbiting_hottest_star_exception(self):

        self.ep.dataset_ = {}
        self.assertEqual(self.ep.get_planet_orbiting_hottest_star(), {})

    def test_get_list_of_orphan_planet_name_exception(self):

        self.ep.dataset_ = [{
            "PlanetIdentifier": "Kepler-1287 b",
            "PlanetaryMassJpt": "",
            "RadiusJpt": 0.137,
            "PeriodDays": 11.47685909,
            "SemiMajorAxisAU": "",
            "Eccentricity": "",
            "PeriastronDeg": "",
            "LongitudeDeg": "",
            "AscendingNodeDeg": "",
            "InclinationDeg": "",
            "SurfaceTempK": "",
            "AgeGyr": "",
            "DiscoveryMethod": "transit",
            "DiscoveryYear": 2016,
            "LastUpdated": "16/05/10",
            "RightAscension": "19 16 32",
            "Declination": "+47 03 47",
            "DistFromSunParsec": "",
            "HostStarMassSlrMass": 0.96,
            "HostStarRadiusSlrRad": 0.94,
            "HostStarMetallicity": -0.05,
            "HostStarTempK": 5715,
            "HostStarAgeGyr": ""
        }]

        self.assertEqual(self.ep.get_list_of_orphan_planet_name(), [])

    def test_get_timeline_with_empty_dataset(self):

        self.ep.dataset_ = {}
        self.assertEqual(self.ep.get_planet_timeline(), {})


if __name__ == '__main__':
    unittest.main()
