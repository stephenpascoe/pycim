"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pycim.v1_5.types import *
from pycim_test.test_utils import *


# Module provenance info.
__author__="markmorgan"
__date__ ="$Aug 31, 2010 11:43:27 AM$"
__copyright__ = "Copyright 2011 - Metafor Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



# Target version of CIM being tested.
CIM = '1.5'

# Target type being tested.
TYPE = Platform

# Test XML representation.
XML_FILE = 'grids.grid_spec'


class TestDecodePlatform(unittest.TestCase):
    """A decoding from xml unit test.

    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_open_xml(self):
        xml = get_test_xml_file(CIM, XML_FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(CIM, XML_FILE, TYPE)
        
        assert obj.cim_info.id == uuid.UUID('b464433a-d3a5-11df-837f-00163e9152a5')
        assert obj.cim_info.version == '2'
        assert obj.cim_info.create_date == dateutil_parser.parse('2012-03-06 10:06:42.266723')

        assert obj.long_name == 'RCP2.6'
        assert obj.short_name == 'rcp26'
        assert obj.description.startswith('Future projection (2006-2100) forced by RCP2.6.')



    def test_representation_dict(self):
        d = decode_dict_from_xml(CIM, XML_FILE, TYPE)
        # TODO
        

    def test_representation_json(self):
        do_test_from_xml_file(CIM, XML_FILE, 'json')


    def test_representation_base64(self):
        do_test_from_xml_file(CIM, XML_FILE, 'base64')


    def test_representation_binary(self):
        do_test_from_xml_file(CIM, XML_FILE, 'binary')

