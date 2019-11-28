import unittest

from odmltools.importers.import_datacite import camel_to_snake


class TestSection(unittest.TestCase):
    def setUp(self):
        pass

    def test_camel_to_snake(self):
        camel = "GeoLocationPoint"
        snake = "geo_location_point"

        conv = camel_to_snake(camel)
        self.assertEqual(conv, snake)
