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
XML_FILE = 'shared.platform.xml'


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
        
        assert obj.cim_info.id == uuid.UUID('b765775a-e2ac-11df-9efb-00163e9152a5')
        assert obj.cim_info.version == '1'
        assert obj.cim_info.create_date == dateutil_parser.parse('2012-03-01 13:55:56.232228')

        assert obj.description is None
        assert obj.long_name == 'Machine IBM Power 6 and compiler Other'
        assert obj.short_name == 'IBM Power 6_Other'

        assert len(obj.contacts) == 1
        assert obj.contacts[0].abbreviation == 'MOHC'
        assert obj.contacts[0].organisation_name == 'UK Met Office Hadley Centre'
        assert obj.contacts[0].role == 'contact'
        
        assert len(obj.units) == 1
        assert obj.units[0].machine is not None
        assert obj.units[0].machine.cores_per_processor == 32
        assert obj.units[0].machine.description is None
        assert obj.units[0].machine.interconnect == 'Infiniband'
        assert obj.units[0].machine.name == 'IBM Power 6'
        assert len(obj.units[0].machine.libraries) == 0
        assert obj.units[0].machine.location is None
        assert obj.units[0].machine.maximum_processors == 2
        assert obj.units[0].machine.operating_system == 'AIX'
        assert obj.units[0].machine.system == 'Parallel'
        assert obj.units[0].machine.type is None
        assert obj.units[0].machine.vendor == 'IBM'
        assert obj.units[0].machine.processor_type == 'Other'
        assert len(obj.units[0].compilers) == 1
        assert obj.units[0].compilers[0].environment_variables is None
        assert obj.units[0].compilers[0].language is None
        assert obj.units[0].compilers[0].name == 'Other'
        assert obj.units[0].compilers[0].options is None
        assert obj.units[0].compilers[0].type is None
        assert obj.units[0].compilers[0].version == '12.1.0.0'


    def test_representation_dict(self):
        d = decode_dict_from_xml(CIM, XML_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO
        

    def test_representation_json(self):
        do_test_from_xml_file(CIM, XML_FILE, 'json')


    def test_representation_base64(self):
        do_test_from_xml_file(CIM, XML_FILE, 'base64')



