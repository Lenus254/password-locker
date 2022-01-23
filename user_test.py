import unittest
from user import User

class TestUser(unittest.TestCase):
    """define test case for user class behavior"""

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
    def tearDown(self):
        User.user_list = []

         self.new_user = User("Linus","lin","lin@lin","12345") # create user object for test