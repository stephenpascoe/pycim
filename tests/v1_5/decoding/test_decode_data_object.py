"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pycim_test.utils import *

# Module provenance info.
__author__="markmorgan"
__date__ ="$Aug 31, 2010 11:43:27 AM$"
__copyright__ = "Copyright 2011 - Metafor Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Representation being tested.
XML_FILE = 'data_object.xml'



class TestDecodeDataObject(unittest.TestCase):
    """A decoding from xml unit test.

    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_open_xml(self):
        representation = get_test_xml_file(XML_FILE)
        assert representation is not None


    def test_decode_from_xml(self):
        from pycim.cim_serializer import decode
        from pycim.v1_5.types import *

        # Open cim xml file.
        representation = get_test_xml_file(XML_FILE)

        # Decode.
        do = decode(representation, '1.5', 'xml')

        # Test decoded instance.
        assert do is not None
        assert isinstance(do, DataObject)

        assert do.acronym == 'HADGEM2_20C3M_1_D0_hus700'
        assert do.child_object == []
        assert do.cim_info.id == uuid.UUID('834151a4-978d-4627-954e-285916bb907a')
        assert do.cim_info.version == '1'
        assert do.cim_info.create_date == dateutil_parser.parse('2011-09-28T16:08:41')
        for i in range(1):
            c = do.citations[i]
            assert c is not None
            assert isinstance(c, Citation)
            assert c.title.startswith(str(i + 1) + ' - ')
            assert c.date == dateutil_parser.parse('2009-02-11')
        assert len(do.content) == 1
        assert do.content[0].aggregation == 'sum'
        assert do.content[0].frequency == 'Other'
        assert do.content[0].topic.name == 'specific_humidity'
        assert do.content[0].topic.description.find('specific" means per unit mass') >= 0
        assert do.content[0].topic.unit == 'm s-1'
        for i in range(1):
            dp = do.data_property[i]
            assert isinstance(dp, DataProperty)
            assert dp.name == 'TestProperty' + str(i + 1)
            assert dp.value == str(i + 1)
        assert do.data_status == 'complete'
        assert do.description.startswith('This dataset represents daily output: instantaneous daily')
        assert do.distribution.access == 'OnlineFileHTTP'
        assert do.distribution.format == 'NetCDF'
        assert do.distribution.responsible_party.individual_name == 'Met Office (HC)'
        assert do.distribution.responsible_party.organisation_name == 'Hadley Centre'
        assert do.distribution.responsible_party.role == 'distributor'
        assert do.extent.geographical.east == float(360)
        assert do.extent.geographical.south == float(-90)
        assert do.extent.geographical.west == float(0)
        assert do.extent.geographical.north == float(90)
        assert do.extent.temporal.begin == dateutil_parser.parse('1859-12-1')
        assert do.extent.temporal.end == dateutil_parser.parse('1999-12-30')
        assert do.extent.temporal.time_interval.factor == int(-1)
        assert do.extent.temporal.time_interval.radix == int(50430)
        assert do.extent.temporal.time_interval.unit == 'day'
        assert do.geometry_model is None
        assert do.hierarchy_level.name == 'experiment'
        assert do.hierarchy_level.value == 'HADGEM2_20C3M_1_D0_hus700'
        assert do.hierarchy_level.is_open == True
        assert do.keyword == 'Test keyword'        
        assert do.parent_object is None
        assert do.parent_object_reference is None
        assert do.purpose == 'test'
        assert len(do.restriction) == 0
        assert do.source_simulation is None
        assert len(do.storage) == 0


    def test_representation_dict(self):
        from pycim.cim_serializer import decode
        from pycim.v1_5.types import *

        # Open cim xml file.
        representation = get_test_xml_file(XML_FILE)

        # Decode.
        do = decode(representation, '1.5', 'xml')

        # Convert.
        d = do.as_dict()

        # Test dictionary derived from decoded object.
        assert d is not None
        assert isinstance(d, dict)
        
        assert d['acronym'] == 'HADGEM2_20C3M_1_D0_hus700'
        assert d['cim_info']['id'] == uuid.UUID('834151a4-978d-4627-954e-285916bb907a')
        assert len(d['content']) == 1
        assert d['extent']['temporal']['begin'] == dateutil_parser.parse('1859-12-1')


    def test_representation_json(self):
        do_representation_test_from_xml_file(XML_FILE, '1.5','json')


    def test_representation_base64(self):
        do_representation_test_from_xml_file(XML_FILE, '1.5', 'base64')


    def test_representation_binary(self):
        do_representation_test_from_xml_file(XML_FILE, '1.5', 'binary')