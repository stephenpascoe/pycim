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
TYPE = NumericalExperiment

# Test XML representation.
XML_FILE = 'activity.numericalExperiment.xml'


class TestDecodeNumericalExperiment(unittest.TestCase):
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

        assert len(obj.rationales) == 1
        assert obj.rationales[0].startswith('Provide estimate of future antrhopogenic')

        assert obj.experiment_id == '4.3'

        assert len(obj.requirements) == 8
        assert obj.requirements[0].id == 'ic.004'
        assert obj.requirements[0].name == '4.3.ic'
        assert obj.requirements[0].description.startswith('Initial conditions are from the end of')
        assert obj.requirements[1].name == '4.3.bc.wmg'
        assert obj.requirements[1].description.startswith('Imposed changing concentrations or emissions')
        assert len(obj.requirements[1].options) == 2
        assert obj.requirements[1].options[0].relationship == 'XOR'
        assert obj.requirements[1].options[0].requirement.id == 'bc.076'
        assert obj.requirements[1].options[0].requirement.name == '4.3.bc.wmg_conc'
        assert obj.requirements[1].options[0].requirement.description == 'Concentrations'
        assert obj.requirements[1].options[1].relationship == 'XOR'
        assert obj.requirements[1].options[1].requirement.id == 'bc.080'
        assert obj.requirements[1].options[1].requirement.name == '4.3.bc.wmg_em'
        assert obj.requirements[1].options[1].requirement.description == 'Emissions'
        assert obj.requirements[2].name == '4.3.bc.sls_conc'
        assert obj.requirements[2].description.startswith('Imposed changing concentrations or emissions')
        assert obj.requirements[3].name == '4.3.bc.aer'
        assert obj.requirements[3].description.startswith('Imposed changing concentrations or emissions')
        assert obj.requirements[4].name == '4.3.bc.aer_pre'
        assert obj.requirements[4].description.startswith('Imposed changing concentrations or emissions')
        assert obj.requirements[5].name == '4.3.bc.LU'
        assert obj.requirements[5].description.startswith('Imposed changing RCP2.6')
        assert obj.requirements[6].name == '4.3.bc.volc_aer_conc'
        assert obj.requirements[6].description.startswith('Imposed constant background')
        assert obj.requirements[7].name == '4.3.stc.2006_94yr'
        assert obj.requirements[7].description.startswith('Begin in 2006 and run')
        assert obj.requirements[7].date_range is not None
        assert obj.requirements[7].date_range.duration == 'P94Y'
        assert obj.requirements[7].date_range.end == dateutil_parser.parse('2100-01-01 00:00:00Z')
        assert obj.requirements[7].date_range.start == dateutil_parser.parse('2006-01-01 00:00:00Z')


    def test_representation_dict(self):
        d = decode_dict_from_xml(CIM, XML_FILE, TYPE)
        # TODO
        

    def test_representation_json(self):
        do_test_from_xml_file(CIM, XML_FILE, 'json')


    def test_representation_base64(self):
        do_test_from_xml_file(CIM, XML_FILE, 'base64')


    def test_representation_binary(self):
        do_test_from_xml_file(CIM, XML_FILE, 'binary')

