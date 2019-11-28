"""
test_importers_datacite_integration tests parsing
whole datacite xml files.
"""

import os
import shutil
import tempfile
import unittest

import odml
import odmltools.importers.import_datacite as dimp


class TestDataciteIntegration(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.resources = os.path.join(dir_path, "resources")

        self.tmp_dir = tempfile.mkdtemp(suffix=".odmltools")

    def tearDown(self):
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

    def test_complete_conversion(self):
        # This test should be split up into multiple tests
        # but for now converting a complete datacite xml
        # file to odml should at least not break when
        # changes to the code are made.

        invalid_file = os.path.join(self.resources, "noxml.md")
        with self.assertRaises(dimp.ParserException):
            _ = dimp.dict_from_xml(invalid_file)

        dc_fn = "fullDataCiteSchema.xml"
        dc_file = os.path.join(self.resources, dc_fn)
        dimp.handle_document(dc_file, self.tmp_dir)

        # make sure the file has been created and is an accessible odml file
        doc = odml.load(os.path.join(self.tmp_dir, dc_fn))
        self.assertGreater(len(doc), 0)
