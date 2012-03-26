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
TYPE = SimulationRun

# Test XML representation.
XML_FILE = 'activity.simulationRun.xml'


class TestDecodeSimulationRun(unittest.TestCase):
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

        assert obj.cim_info.id == uuid.UUID('309862aa-6dc0-11e1-b0dd-00163e9152a5')
        assert obj.cim_info.version == '1'
        assert obj.cim_info.create_date == dateutil_parser.parse('2012-03-14 10:27:35.614481')
        assert obj.cim_info.author.individual_name == 'Metafor Questionnaire'
        assert len(obj.cim_info.external_ids) == 1
        assert obj.cim_info.external_ids[0].is_open == True
        assert obj.cim_info.external_ids[0].value == 'CMCC_CMCC-CM_1.1 decadal1965'
        assert len(obj.cim_info.external_ids[0].standards) == 1
        assert obj.cim_info.external_ids[0].standards[0].name == 'QN_DRS'
        assert obj.cim_info.external_ids[0].standards[0].description.startswith('The QN_DRS value')
        
        assert obj.long_name == None
        assert obj.short_name == 'CMCC-CM_decadal2000'
        assert obj.description.startswith('10-year run initialized in November 2000')

        assert obj.authors == 'Silvio Gualdi, Alessio Bellucci'

        assert len(obj.deployments) == 1
        assert obj.deployments[0].description.startswith('The resources(deployment) on which this simulation ran')
        assert obj.deployments[0].platform == None
        assert obj.deployments[0].platform_reference is not None
        assert obj.deployments[0].platform_reference.id == uuid.UUID('d0f22fe6-6dbc-11e1-9bbb-00163e9152a5')
        assert obj.deployments[0].platform_reference.name == 'calypso'
        assert obj.deployments[0].platform_reference.type == 'platform'
        assert obj.deployments[0].platform_reference.version == '1'
        assert obj.deployments[0].platform_reference.description == 'Reference to a platform called calypso'

        assert isinstance(obj.date_range, ClosedDateRange)
        assert obj.date_range.duration == 'P10Y'
        assert obj.date_range.start == dateutil_parser.parse('2000-11-01 00:00:00Z')

        assert obj.model == None
        assert obj.model_reference is not None
        assert obj.model_reference.id == uuid.UUID('9a85d330-6c2d-11e1-8021-00163e9152a5')
        assert obj.model_reference.name == 'CMCC-CM'
        assert obj.model_reference.type == 'modelComponent'
        assert obj.model_reference.version == '1'
        assert obj.model_reference.description == 'Reference to a modelComponent called CMCC-CM'

        assert len(obj.projects) == 1
        assert obj.projects[0] == 'CMIP5'

        assert len(obj.responsible_parties) == 4
        rp = obj.responsible_parties[0]
        assert rp.abbreviation == 'sgualdi'
        assert rp.contact_info.email == 'silvio.gualdi@cmcc.it'
        assert rp.individual_name == 'Silvio Gualdi'
        assert rp.role == 'contact'


    def test_representation_dict(self):
        d = decode_dict_from_xml(CIM, XML_FILE, TYPE)
        # TODO


    def test_representation_json(self):
        do_test_from_xml_file(CIM, XML_FILE, 'json')


    def test_representation_base64(self):
        do_test_from_xml_file(CIM, XML_FILE, 'base64')


    def test_representation_binary(self):
        do_test_from_xml_file(CIM, XML_FILE, 'binary')

