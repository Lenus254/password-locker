import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("linus","lin","lin@lin","12345") # create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []



    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"linus")
        self.assertEqual(self.new_user.last_name,"lin")
        self.assertEqual(self.new_user.user_name,"lin@lin")
        self.assertEqual(self.new_user.password,"12345")
