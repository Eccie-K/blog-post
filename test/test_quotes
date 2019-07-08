import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1234,'Smith','A thrilling new Python Series','/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))