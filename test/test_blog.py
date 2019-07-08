import unittest
from app.models import Source

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''

    def setUp(self):

        '''
        Set up method that will run before every Test
        '''
        self.new_blog =Blog(None,'Blog')

    def test_instance(self):

        self.assertTrue(instance(self.new_blog,Blog))

if __name__ == '__main__':
  unittest.main()
