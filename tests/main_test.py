import unittest

from polygon_geohasher.polygon_geohasher import (
    polygon_to_geohashes,
    geohash_to_polygon,
    geohashes_to_polygon,
)
from shapely import geometry


class TestSimpleMethods(unittest.TestCase):
    def test_one_geohash(self):
        test_geohash = "x1"
        test_polygon = geohash_to_polygon(test_geohash)
        polygon = geohashes_to_polygon(polygon_to_geohashes(test_polygon, 2))

        self.assertEqual(test_polygon.area, polygon.area)
        self.assertTrue(test_polygon.covers(test_polygon.intersection(polygon)))
        self.assertTrue(test_polygon.intersection(polygon).covers(test_polygon))

    def test_triangle(self):
        test_polygon = geometry.Polygon(
            [
                (-99.1795917, 19.432134),
                (-99.1656847, 19.429034),
                (-99.1776492, 19.414236),
                (-99.1795917, 19.432134),
            ]
        )

        geohashes = polygon_to_geohashes(test_polygon, 7)
        self.assertEqual(geohashes,
                         {'9g3qrpj', '9g3qrpn', '9g3qx0r', '9g3qx2b', '9g3qx23', '9g3qx2g', '9g3qrpq', '9g3qx22',
                          '9g3qrpw', '9g3qx1p', '9g3qx26', '9g3qx0z', '9g3qrpr', '9g3qx0p', '9g3qrpx', '9g3qx28',
                          '9g3qx0n', '9g3qx2c', '9g3qx0x', '9g3qx20', '9g3qrpt', '9g3qrr8', '9g3qrpv', '9g3qx2f',
                          '9g3qx2e', '9g3qx0q', '9g3qrpm', '9g3qx0m', '9g3qrpy', '9g3qx21', '9g3qrnv', '9g3qx0t',
                          '9g3qx1n', '9g3qx1h', '9g3qx2d', '9g3qx0j', '9g3qx29', '9g3qx0y', '9g3qx0w', '9g3qx0v',
                          '9g3qx1j', '9g3qrpz', '9g3qx0u', '9g3qrrb'})
        polygon = geohashes_to_polygon(geohashes)
        self.assertTrue(polygon.area <= test_polygon.area)
        self.assertTrue(
            all(polygon.covers(geometry.Point(c)) for c in polygon.boundary.coords)
        )
        polygon = geohashes_to_polygon(polygon_to_geohashes(test_polygon, 7, False))
        self.assertTrue(polygon.area >= test_polygon.area)


if __name__ == "__main__":
    unittest.main()
